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
    if len(self.password) == 0 or len(self.userInfo) == 0:
      return (0, '')

    self.calculate()
    longestCoincidence = self.saved[-1][-1]
    indices = longestCoincidence.getCoincidenceIndices()
    return (longestCoincidence.value, self.getCoincidenceFromIndices(indices))


userInfo = ['rksmith', 'rick', 'smith', 'raks', '']

password = 'r_1ksmi7t'

for info in userInfo:
  checker = PasswordChecker(info, password)
  print(info)
  print(checker.getLongestCoincidence())

  # for k in checker.saved:
  #   print([j.value for j in k])
