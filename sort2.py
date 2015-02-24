import random

def randlist(size):
  lst=[]
  for i in range(size):
    
    i= random.randrange(0, size)
    lst.append(i)
  return lst

def bubblesort(lst):
  switch=True

  while switch:
    switch=False
    for i in range(len(lst)-1):
      if lst[i]>lst[i+1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
        switch=True

def shakersort(lst):
  switch=True

  while switch:
    switch= False
    for i in range(len(lst)-1):
      if lst[i]>lst[i+1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
        switch= True    
    for i in range(len(lst)-2, -1, -1):
      if lst[i]>lst[i+1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
        switch= True

def selectionsort(lst):

  for i in range(len(lst)):
    smallest=i
    for j in range(i+1,len(lst)):
      if lst[j]<lst[smallest]:
        smallest=j
    lst[i],lst[smallest]=lst[smallest],lst[i]
             
def main(size):
  originalunsorted=randlist(size)
  originalsorted=originalunsorted[:]
  originalsorted.sort()
  lst1=originalunsorted[:]
  lst2=originalunsorted[:]
  lst3=originalunsorted[:]
  print originalunsorted
  bubblesort(lst1)
  if lst1 != originalsorted:
	print "error"
  else:
    print "bubblesort"
    print lst1
  shakersort(lst2)
  if lst2 != originalsorted:
	print "error"
  else:
    print "shakersort"
    print lst2
  selectionsort(lst3)
  if lst3 != originalsorted:
	print "error"
  else:
    print "selectionsort"
    print lst3

main(10)

