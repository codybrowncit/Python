class Node:
  def __init__(self, mObject, next):
    self.mObject = mObject
    self.mNext = next

class UnorderedUniqueContainer:
  def __init__(self):
    self.mFirst = None
    
  def Insert(self, mObject):
    if not self.Exists(mObject):
      n = Node(mObject, self.mFirst)
      self.mFirst = n
      return True
    return False
    
  def Exists(self, fakeObject):
    current = self.mFirst
    while current is not None:
      if current.mObject == fakeObject:
        return True
      current = current.mNext
    return False

  def Delete(self, fakeObject):
    #print fakeObject.mSSN
    if not self.Exists(fakeObject):
      return False
    # check if it's the first one.
    if self.mFirst.mObject == fakeObject:
      self.mFirst = self.mFirst.mNext
      return True
    # use a look-ahead to see if the next one is == to the fakeObject we are looking for
    current = self.mFirst
    while current.mNext.mObject != fakeObject:
      current = current.mNext
    current.mNext = current.mNext.mNext
    return True

  def Traverse(self, function):
    current = self.mFirst
    while current is not None:
      function(current.mObject)
      current = current.mNext

  def Size(self):
    count = 0
    current = self.mFirst
    while current is not None:
      count += 1
      current = current.mNext
    return count

  def Retrieve(self, fakeObject):
    current = self.mFirst
    while current is not None:
      if current.mObject == fakeObject:
        return current.mObject
      current = current.mNext
    return None
