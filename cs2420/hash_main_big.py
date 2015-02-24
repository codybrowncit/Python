import sys

from student import *
from hash_starter import *
import time

TOTAL_AGE = 0.0

files = {
  'insert': 'InsertNamesBig.txt',
  'retrieve': 'RetrieveNamesBig.txt',
  'delete': 'DeleteNamesBig.txt'
}

def storeAge(student):
  global TOTAL_AGE
  TOTAL_AGE += student.getAge()

def insert(allStudents):
  before = time.time()
  fin = open(files['insert'], "r")
  for line in fin:
    words = line.split()
    s = Student(words)
    if not allStudents.Insert(s):
      continue
  after = time.time()
  print "# of students: %i" % allStudents.Size()
  print "Time taken to insert: %.2f minutes.\n\n" % ((after - before)/60)

def traverse(allStudents):
  before = time.time()
  allStudents.Traverse(storeAge)
  after = time.time()
  print "The average age of all the students is %f" % (TOTAL_AGE/allStudents.Size())
  print "Time taken to traverse: %.2f seconds.\n\n" % (after - before)

def retrieve(allStudents):
  before = time.time()
  totalAge = 0.0
  count = 0
  fin = open(files['retrieve'], "r")
  for line in fin:
    ssn = line.strip()
    blank_student = Student(["", "", ssn, "", "25"])
    found = False
    s = allStudents.Retrieve(blank_student)
    if s:
      found = True
      totalAge += s.getAge()
      count += 1
    #print "No student found with SSN %s." % ssn
  after = time.time()
  if count < 1:
    print "No students retrieved."
  else:
    print "Average age of retrieved students: %f" % (totalAge/count)
  print "Time taken to retrieve: %.2f seconds.\n\n" % (after - before)

def delete(allStudents):
  before = time.time()
  fin = open(files['delete'], "r")
  for line in fin:
    ssn = line.strip()
    blank_student = Student(["", "", ssn, "", "25"])
    if allStudents.Delete(blank_student):
      continue
      #print "No student found with SSN %s" % ssn
  after = time.time()
  print "Number of Students, now: %s" % allStudents.Size()
  print "Time taken to delete: %.2f seconds.\n\n" % (after - before)

def main():
  allStudents = Hash(300000)
  insert(allStudents)
  traverse(allStudents)
  retrieve(allStudents)
  delete(allStudents)

main()
