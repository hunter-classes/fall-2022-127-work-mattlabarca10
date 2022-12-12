# takes in a list of numbers and returns the value of the smallest number
from operator import indexOf


def findLargest(l):
    max = l[0]
    for x in l: 
        if x>max: max = x
    return max

print(findLargest([7,3,2,56,7,2,6]))

# takes a list of numbers (l) and a value (v). The function will return the freuqeency 
# of v, that is, the number of times that v appears in l
def freq(l,v):
   # count = 0
    #for x in l:
     #   if x == v: count +=1
    #return count
    return len([x for x in l if x==v])

print(freq([3,6,2,7,2,6,78,8,2,1,5,6,3,7],6))

def mode(dataset):
    modeSoFar = dataset[0]
    freqSoFar = freq(dataset,modeSoFar)
    for item in dataset[1:]:
        if freq(dataset,item) > freqSoFar:
            modeSoFar = item
            freqSoFar = freq(dataset,item)
    return modeSoFar
print(mode([6,2,7,2,6,78,8,2,1,5,6,3,7]))

# def testMode(size,maxValue):

import datetime
import random

def fastMode(dataset):
    list = [0]*100
    for num in dataset:
        list[num]+=1
    return list.index(findLargest(list))

print(fastMode([6,2,7,2,6,78,8,2,1,5,6,3,2,7]))

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 




"""
def testMode(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = mode(dataset)
    print("Mode: ",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)

#testFindLargest(80000,30)
testMode(40000,30)
"""