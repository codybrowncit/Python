import time

class Student:
  def __init__(self, words):
    self.mLast = words[0]
    self.mFirst = words[1]
    self.mSSN = words[2][:3]+words[2][4:6]+words[2][7:]
    self.SSN_is_valid()
    self.mEmail = words[3]
    self.mAge = int(words[4])

  def SSN_is_valid(self):
    if len(self.mSSN) != 9:
      print "Invalid SSN: %s" % self.mSSN
  def getAge(self):
    return self.mAge

  def __str__(self):
    return "%s, %s" % (self.mLast.capitalize(), self.mFirst.capitalize())

  def __eq__(self, rhs):
    #rhs = right hand side.
    # use this to compare two Student objects with the s1 == s2 notation.
    if rhs == None or rhs == False:
      return False
    return self.mSSN == rhs.mSSN

  def __ne__(self, rhs):
    if rhs == None or rhs == False:
      return False
    return self.mSSN != rhs.mSSN

  

  def __lt__(self, rhs):
    return self.mSSN < rhs.mSSN

  def __gt__(self, rhs):
    return self.mSSN < rhs.mSSN

  def __int__(self):
    return int(self.mSSN)

def Insert(allStudents):
  before = time.time()
  fin = open("InsertNames.txt", "r")
  for line in fin:
    words = line.split() # gets the 5 items in a list, each item at its own index.
    s = Student(words)
    unique = True
    for s2 in allStudents:
      if s == s2:
        print "Duplicate record: %s" % s
        unique = False
    if unique:
      allStudents.append(s)

  after = time.time()
  print "It took %.2f minutes to insert." % ((after - before)/60)
  print "There are %s students.\n" % len(allStudents)

def Traverse(allStudents):
  before = time.time()
  totalAge = 0.0
  # should end up being 42.something
  for s in allStudents:
    totalAge += s.getAge()
  after = time.time()
  print "The average age of all the students is %f" % (totalAge/len(allStudents))
  print "It took %.2f seconds to Traverse.\n" % (after - before)

def Delete(allStudents):
  before = time.time()
  fin = open("DeleteNames.txt", "r")
  for line in fin:
    ssn = line.strip()
    blank_student = Student(["", "", ssn, "", "25"])
    found = False
    for i in range(len(allStudents)):
      if allStudents[i] == blank_student:
        found = True
        allStudents.pop(i)
        break
    if not found:
      print "No student found with SSN %s." % ssn
  after = time.time()
  print "There are now %s students" % len(allStudents)
  print "It took %.2f seconds to delete.\n" % (after - before)

def Retrieve(allStudents):
  before = time.time()
  fin = open("RetrieveNames.txt", "r")
  totalAge = 0.0
  count = 0
  for line in fin:
    ssn = line.strip()
    blank_student = Student(["", "", ssn, "", "25"])
    found = False
    for i in range(len(allStudents)):
      if allStudents[i] == blank_student:
        found = True
        totalAge += allStudents[i].getAge()
        count += 1
        break
    if not found:
      print "No student found with SSN %s." % ssn
  after = time.time()
  print "Average age of retrieved students is %f" % (totalAge/count)
  print "It took %.2f seconds to retrieve.\n" % (after - before)

def main():
  allStudents = []
  Insert(allStudents)
  Traverse(allStudents)
  Retrieve(allStudents)
  Delete(allStudents)

if __name__ == "__main__":
  main()
