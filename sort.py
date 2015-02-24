import random
import sys
import math

def randlist(size):
  lst=[]
  for i in range(size):
    
    i= random.randrange(0, size)
    lst.append(i)
  return lst

def bubblesort(lst, compare):
  switch=True
  while switch:
    switch=False

    for i in range(len(lst)-1):
      compare[0]+=1
      if lst[i]>lst[i+1]:
        compare[1]+=1
        lst[i],lst[i+1]=lst[i+1],lst[i]
        switch=True

def shakersort(lst, compare):
  switch=True
  while switch:
    switch= False
    for i in range(len(lst)-1):
      compare[0]+=1
      if lst[i]>lst[i+1]:
        compare[1]+=1
        lst[i],lst[i+1]=lst[i+1],lst[i]
        switch= True    
    for i in range(len(lst)-2, -1, -1):
      compare[0]+=1
      if lst[i]>lst[i+1]:
        compare[1]+=1
        lst[i],lst[i+1]=lst[i+1],lst[i]
        switch= True

def selectionsort(lst, compare):
  for i in range(len(lst)):
    smallest=i
    for j in range(i+1,len(lst)):
      compare[0]+=1
      if lst[j]<lst[smallest]:
        smallest=j
    compare[1]+=1
    lst[i],lst[smallest]=lst[smallest],lst[i]

def quick(lst, low, high, modified, compare):
  if high-low<0:
    return
  if modified:
    pivot=random.randint(low, high)
    lst[low],lst[pivot]=lst[pivot],lst[low]
    compare[1]+=1
  else:
    pivot=low
  x=low+1
  pivot=lst[low]
  for i in range(low+1, high+1):
    compare[0]+=1
    if lst[i]<pivot:
      lst[i],lst[x]= lst[x],lst[i]
      compare[1]+=1
      x+=1
  position=x-1
  lst[position],lst[low] = lst[low],lst[position]
  compare[1]+=1
  if low<high:
    quick(lst, low, position-1, modified, compare)
    quick(lst, position+1, high, modified, compare)
    
  

def quicksort(lst, compare):
  quick(lst, 0, len(lst)-1, False, compare)

def quicksortmodified(lst, compare):
  quick(lst, 0, len(lst)-1, True, compare)

def mergesort(lst, compare):
  if len(lst)<=1:
    return
  midpoint=len(lst)/2
  left=lst[:midpoint]
  right=lst[midpoint:]
  compare[1] += len(lst)
  mergesort(left, compare)
  mergesort(right, compare)
  a=0
  l=0
  r=0
  while a<len(lst):
    if l>=len(left):
      lst[a]=right[r]
      a+=1
      r+=1
    elif r>=len(right):
      lst[a]=left[l]
      a+=1
      l+=1
    elif left[l]<=right[r]:
      lst[a]=left[l]
      a+=1
      l+=1
    else:
      lst[a]=right[r]
      a+=1
      r+=1
  compare[0]+=len(lst)
  compare[1]+=len(lst)

def hashsort(lst, compare):
  f=[0]*len(lst)
  for i in range(len(lst)):
    compare[0]+=1
    value=lst[i]
    f[value]+=1
  lindex=0
  for j in range(len(f)):
    count=f[j]
    for k in range (count):
      compare[1]+=1
      lst[lindex]=j
      lindex+=1

def Format(x):
  if x!=0:
    x = math.log(x)/math.log(2)
    x = "%5.3f" % x
  #x *= 100
  #x = int(x)
  #x = float(x)
  #x /= 100
  return x

def main():
  startingSize = 8
  endingSize = 1024*4

  sys.setrecursionlimit(endingSize+10)
 
  WhatToCount = ["Compares","Swaps"]
  KindOfData = ["Random", "Mostly Sorted"]
  sortAlgorithms=[bubblesort,shakersort,selectionsort,quicksort,quicksortmodified,mergesort,hashsort]
  sortNames=["Bubble Sort","Shaker Sort","Selection Sort","Quick Sort","Modified Quick Sort","Merge Sort","Hash Sort"]
  for dataType in KindOfData:
    for countType in WhatToCount:
      print "\nCounting",countType,"On",dataType,"Data"
      print "\t"
      for name in sortNames:
        print "\t"+name,
      print

      size = startingSize
      while size<= endingSize:

        print Format(size),
        for i in range(len(sortAlgorithms)):
           compare= [0,0]
           sort=sortAlgorithms[i]
           lst=randlist(size)
           if dataType=="Mostly Sorted":
             lst.sort()
             temp=lst[0]
             lst[0]=lst[-1]
             lst[-1]=temp
           sort(lst, compare)
           if countType=="Compares":
             print "\t"+Format(compare[0]),
           else:
             print "\t"+Format(compare[1]),
        print
        size+=size
           
         
    
  
 

main()

