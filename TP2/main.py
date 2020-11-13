class Node():
  def __init__(self, value=0, index=-1, prev=None):
    self.value = value
    self.index = index
    self.prev = prev

  def __gt__(self, other):
    return self.value > other.value

  def getCoincidenceIndices(self):
    node = self.prev
    indices = [self.index] if self.prev.value < self.value else []

    while(node and node.value > 0):
      if (node.prev.value < node.value):
        indices.insert(0, node.index)

      node = node.prev

    return indices


class PasswordChecker():
  def __init__(self, userInfo, password):
    self.userInfo = userInfo
    self.password = password
    self.longestCoincidence = Node()
    self.saved = [[Node() for k in range(len(password))]
                  for i in range(len(userInfo))]

  def save(self, userInfoIndex, passwordIndex, value):
    self.saved[userInfoIndex][passwordIndex] = value

  def getSavedValue(self, userInfoIndex, passwordIndex):
    if userInfoIndex < 0 or passwordIndex < 0:
      return Node()
    else:
      return self.saved[userInfoIndex][passwordIndex]

  def calculate(self):
    for i in range(len(self.userInfo)):
      for k in range(len(self.password)):
        if (self.password[k] == self.userInfo[i]):
          prev = self.getSavedValue(i - 1, k - 1)
          self.saved[i][k] = max(Node(1 + prev.value, k, prev), self.getSavedValue(i - 1, k))
        else:
          self.saved[i][k] = max(self.getSavedValue(i, k - 1), self.getSavedValue(i - 1, k))

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

password = 'r_1kksmi7t'

for info in userInfo:
  checker = PasswordChecker(info, password)
  print(info)
  print(checker.getLongestCoincidence())

  for k in checker.saved:
    print([j.value for j in k])
