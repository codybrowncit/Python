


from student import *
import time
from LinkedList import *

TOTAL_AGE = 0.0

def storeAge(student):
  global TOTAL_AGE
  TOTAL_AGE += student.getAge()

def insert(allStudents):
  before = time.time()
  fin = open("InsertNamesBig.txt", "r")
  for line in fin:
    words = line.split()
    s = Student(words)
    if not allStudents.Insert(s):
      print "Duplicate found: %s." % s
  after = time.time()
  print "There are %i students." % allStudents.Size()
  print "It took %.2f minutes to insert.\n\n" % ((after - before)/60)

def traverse(allStudents):
  before = time.time()
  allStudents.Traverse(storeAge)
  after = time.time()
  print "The average age of all the students is %f" % (TOTAL_AGE/allStudents.Size())
  print "It took %.2f seconds to traverse.\n\n" % (after - before)

def retrieve(allStudents):
  before = time.time()
  totalAge = 0.0 
  count = 0
  fin = open("RetrieveNamesBig.txt", "r")
  for line in fin:
    ssn = line.strip()
    blank_student = Student(["", "", ssn, "", "25"])
    found = False
    s = allStudents.Retrieve(blank_student)
    if s:
      found = True
      totalAge += s.getAge()
      count += 1
  if not found:
    print "No student found with SSN %s." % ssn
  after = time.time()
  if count < 1:
    print "No students retrieved."
  else:
    print "The average age of retrieved students is %f" % (totalAge/count)
  print "It took %.2f seconds to retrive.\n\n" % (after - before)

def delete(allStudents):
  before = time.time()
  fin = open("DeleteNamesBig.txt", "r")
  for line in fin:
    ssn = line.strip()
    blank_student = Student(["", "", ssn, "", "25"])
    found = False
    #print "SSN before deletion."
   # print ssn
    if allStudents.Delete(blank_student):
     # print "Deleted %s" % ssn
      found = True
    else:
      print "%s not found" % ssn

  if not found:
    print "No student found with SSN %s" % ssn
  after = time.time()
  print "There are now %s students" % allStudents.Size()
  print "It took %.2f seconds to delete.\n\n" % (after - before)

def main():
  allStudents = UnorderedUniqueContainer()
  insert(allStudents)
  allStudents_copy = allStudents
  traverse(allStudents)
  retrieve(allStudents)
  delete(allStudents_copy)

main()
