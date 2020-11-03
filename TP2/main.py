class Node():
  def __init__(self, value=0, index=-1, prev=None):
    self.value = value
    self.index = index
    self.prev = prev

  def __gt__(self, other):
    return self.value > other.value

  def getStartAndEndIndex(self):
    node = self.prev
    start = self.index
    end = self.index

    while(node and node.value > 0):
      start = node.index
      node = node.prev

    return (start, end)

class PasswordChecker():
  def __init__(self, userInfo, password):
    self.userInfo = userInfo
    self.password = password
    self.longestCoincidence = Node()
    self.saved = [[Node() for k in range(len(password))] for i in range(len(userInfo))]

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
          self.saved[i][k] = Node(1 + prev.value, k, prev)
        else:
          self.saved[i][k] = self.getSavedValue(i, k - 1)

  def getLongestCoincidence(self):
    if len(self.password) == 0 or len(self.userInfo) == 0:
      return (0, '')

    self.calculate()
    longestCoincidence = max([k[-1] for k in self.saved])
    start, end = longestCoincidence.getStartAndEndIndex()
    return (longestCoincidence.value, self.password[start:end + 1])

userInfo = ['rksmith', 'rick', 'smith', '']

password = 'r_1kcksmi7t'

for info in userInfo:
  checker = PasswordChecker(info, password)
  print(info)
  print(checker.getLongestCoincidence())

  for k in checker.saved:
    print([j.value for j in k])
