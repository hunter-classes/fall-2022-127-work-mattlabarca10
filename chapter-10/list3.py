#5
#Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)

def max(intlist):
    max = intlist[0]
    for int in intlist:
      if int > max:
        max = intlist[int]
    return max

alist=[9,6,4,7]
print(max(alist))

#7
#Write a function to count how many odd numbers are in a list.

def oddNumbers(intlist):
    oddCount = 0
    for int in intlist:
      if int % 2 == 1:
        oddCount = oddCount + 1
    return oddCount

blist=[9,6,4,7]
print(oddNumbers(blist))

#8
#Sum up all the even numbers in a list.

def evenNumberSum(intlist):
    sum = 0
    for int in intlist:
      if int % 2 == 0:
        sum = sum + int
    return sum

clist = [9,6,4,7,2,3,1,6]
print(evenNumberSum(clist))