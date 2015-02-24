class Hash:
  def __init__(self, size):
    self.mTablesize = size*2 + 1
    while not isPrime(self.mTablesize):
      self.mTablesize += 2
    self.mTable = [None]*self.mTablesize
    self.mSize = 0

  def Size(self):
    return self.mSize

  def Exists(self, item):
    key = int(item)
    index = key % self.mTablesize
    exists = False
    while not exists:
      if self.mTable[index] == None:
        return False
      if not self.mTable[index]:
        index += 1
      if self.mTable[index] == item:
        return True
      index += 1
      if index >= self.mTablesize:
        index -= self.mTablesize

  def Traverse(self, callback):
    for i in self.mTable:
      if i is not None:
        callback(i)

  def Retrieve(self, item):
    key = int(item)
    if not self.Exists(item):
      return None
    index = key % self.mTablesize
    while True:
      if self.mTable[index] and self.mTable[index] == item:
        return self.mTable[index]
      index += 1
      if index == len(self.mTable):
        index = 0

  def Insert(self, item):
    key = int(item)
    if self.Exists(item):
      return False
    index = key % self.mTablesize
    while self.mTable[index] is not None:
      index += 1
      if index == self.mTablesize:
        index = 0
    self.mTable[index] = item
    self.mSize += 1
    return True

  def Delete(self, item):
    key = int(item)
    if not self.Exists(item):
      return False
    index = key % self.mTablesize
    while self.mTable[index] is None or self.mTable[index] != item:
      index += 1
      if index == len(self.mTable):
        index = 0
    self.mSize -= 1
    self.mTable[index] = False
    return True

def isPrime(x):
  if x == 2 or x == 1:
    return True
  if not x & 1:
    return False
  sqrt = int(x**.5)
  for i in range(3, sqrt+2, 2):
    if x%i == 0:
      return False
  return True