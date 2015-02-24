class Node:
  def __init__(self, object, left=None, right=None):
    self.mObject = object
    self.mLeft = left
    self.mRight = right

class BinarySearchTree:
  def __init__(self):
    self.mRoot = None
    self.mSize = 0

  def Exists(self, item):
    return self.exists_r(item, self.mRoot)

  def exists_r(self, item, current):
    if not current:
      return False
    if item == current.mObject:
      return True
    if item < current.mObject:
      return self.exists_r(item, current.mLeft)
    return self.exists_r(item, current.mRight)

  def Retrieve(self, item):
    return self.retrieve_r(item, self.mRoot)

  def retrieve_r(self, item, current):
    if not current:
      return None
    if item == current.mObject:
      return current.mObject
    if item < current.mObject:
      return self.retrieve_r(item, current.mLeft)
    return self.retrieve_r(item, current.mRight)

  def Insert(self, object):
    if self.Exists(object):
      return False
    n = Node(object)
    self.mRoot = self.insert_r(self.mRoot, n)
    self.mSize += 1
    return True

  def insert_r(self, current, n):
    if current is None:
      current = n
    elif n.mObject < current.mObject:
      current.mLeft = self.insert_r(current.mLeft, n)
    else:
      current.mRight = self.insert_r(current.mRight, n)
    return current

  def Size(self):
    return self.mSize

  def Traverse(self, callback):
    self.traverse_r(self.mRoot, callback)

  def traverse_r(self, current, callback):
    if current:
      self.traverse_r(current.mLeft, callback)
      callback(current.mObject)
      self.traverse_r(current.mRight, callback)

  def Delete(self, item):
    if not self.Exists(item):
      return False
    self.mRoot = self.delete_r(item, self.mRoot)
    self.mSize -= 1
    return True

  def delete_r(self, item, current):
    if item == current.mObject:
      # leaf case
      if not current.mRight and not current.mLeft:
        current = None
      # one left child
      elif not current.mRight:
        current = current.mLeft
      # one right child
      elif not current.mLeft:
        current = current.mRight
      # two children
      else:
        successor = current.mRight
        while successor.mLeft:
          successor = successor.mLeft
        current.mObject = successor.mObject
        current.mRight = self.delete_r(successor.mObject, current.mRight)
    elif item < current.mObject:
      current.mLeft = self.delete_r(item, current.mLeft)
    else:
      self.mRight = self.delete_r(item, current.mRight)
    return current
