# takes in a list of numbers and returns the value of the smallest number
def findLargest(l):
    min = l[0]
    for x in l: 
        if x>min: min = x
    return min

print(findLargest([7,3,2,56,7,2,6]))

# takes a list of numbers (l) and a value (v). The function will return the freuqeency 
# of v, that is, the number of times that v appears in l
def freq(l,v):
    count = 0
    for x in l:
        if x == v: count +=1
    return count

print(freq([3,6,2,7,2,6,78,8,2,1,5,6,3,7],6))