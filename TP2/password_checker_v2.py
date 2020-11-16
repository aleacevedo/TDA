class Node():
  def __init__(self, value=0, index=-1, prev=None):
    self.value = value
    self.index = index
    self.prev = prev

  def __gt__(self, other):
    return self.value > other.value

  def getCoincidenceIndices(self):
    node = self
    indices = []
    while(node and node.value > 0):
      indices.insert(0, node.index)
      node = node.prev

    return indices


class PasswordChecker():
  def __init__(self, userInfo, password):
    self.userInfo = userInfo
    self.password = password
    self.calculated = False
    self.saved = [[Node()] for i in range(len(userInfo))]

  def save(self, userInfoIndex, passwordIndex, value):
    passwordIndex -= self.indexCorrection
    self.saved[userInfoIndex].append(value)

  def getSavedValue(self, userInfoIndex, passwordIndex):
    passwordIndex -= self.indexCorrection

    if userInfoIndex < 0 or passwordIndex < 0:
      return Node()
    else:
      return self.saved[userInfoIndex][passwordIndex]

  def calculate(self):
    self.calculated = True
    for k in range(len(self.password)):
      for i in range(len(self.userInfo)):
        self.indexCorrection = k - 1
        current = Node()
        if self.password[k] == self.userInfo[i]:
          prev = self.getSavedValue(i - 1, k - 1)
          current = Node(1 + prev.value, k, prev)

        maximumNode = max(
          self.getSavedValue(i, k - 1),
          self.getSavedValue(i - 1, k),
          current
        )
        self.save(i, k, maximumNode)
      for i in range(len(self.userInfo)):
        self.saved[i].pop(0)

  def getCoincidenceFromIndices(self, indices):
    i = 0
    marked = []
    opened = False
    for index, letter in enumerate(self.password):
      if i < len(indices) and indices[i] == index:
        i += 1
        if not opened:
          marked = marked + ['(', letter]
          opened = True
        else:
          marked.append(letter)
      else:
        if opened:
          marked = marked + [')', letter]
          opened = False
        else:
          marked.append(letter)
    marked = marked + [')'] if opened else marked
    return ''.join(marked)

  def getLongestCoincidence(self):
    if len(self.password) == 0 or len(self.userInfo) == 0 or not self.calculated:
      return (0, '')

    longestCoincidence = self.saved[-1][-1]
    indices = longestCoincidence.getCoincidenceIndices()
    return (longestCoincidence.value, self.getCoincidenceFromIndices(indices))


class MultiChecker:
  def __init__(self, userInfo, password):
    print("Para el usuario:")
    self.password = password
    self.checkers = {}
    for key in userInfo.keys():
      print("{}: {}".format(key, userInfo[key]))
      self.checkers[key] = PasswordChecker(userInfo[key], self.password)
      self.checkers[key].calculate()
    print()

  def resultOf(self, key):
    userInfo = self.checkers[key].userInfo
    coincidenceLength, coincidence = self.checkers[key].getLongestCoincidence()
    coincidencePercentage = coincidenceLength / len(userInfo) * 100
    print("Comparando {} \"{}\" con password \"{}\"".format(
      key, userInfo, self.password))
    print("La subcadena más larga es: {} → longitud {}".format(
      coincidence, coincidenceLength))
    print("Porcentaje de coincidencia: 100 * {} / {} = {:.2f}%".format(coincidenceLength,
                                                                       len(userInfo), coincidencePercentage))
    print()
    return coincidenceLength

  def result(self):
    longer = -1
    for key in self.checkers.keys():
      aux = self.resultOf(key)
      longer = aux if aux > longer else longer
    originalityPercentage = 100 - (longer / len(self.password) * 100)
    print("Mayor longitud de coincidencia: {}".format(longer))
    print("Longitud password: {}".format(len(self.password)))
    print("Porcentaje de originalidad: 100 - 100 * mayor longitud de coincidencia / longitud password: {}%".format(originalityPercentage))
