# Write a function to find the smallest value in a listKfind smallest in a list of items
def smallest(listKfind):
    smallest = listKfind[0]
    for value in listKfind:
        if value < smallest:
            smallest = value
    return smallest

print(smallest([1,4,2,6,7,3,0]))

# Write a function that returns a new list that contains all the odd items in the original list
def oddNumbers(list):
    oddList = []
    for value in list:
        if value % 2 == 1:
            oddList.append(value)
    return oddList

print(oddNumbers([4,2,4,7,3,1,63,9]))

# Write a function that takes a string and returns a new string where all the words are capitalized.
def capitalize(string):
    newString = ""
    for word in string.split():
        newString = newString + word.capitalize() + " "
    return newString

print(capitalize("Hello everyone my name is Matthew"))

# Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
def fiveLettersUpper(string):
    newString = ""
    for word in string.split():
        count = 0
        for letters in word:
            count = count + 1
        if count >= 5:
            newString = newString + word.upper() + " "
        else:
            newString = newString + word + " "
    return newString

print(fiveLettersUpper("Hello everyone my name is Matthew"))

# Write a function that takes a list of numbers and returns a new list with each item squared
def squared(numList):
    newList = []
    for num in numList:
        newList.append(num**2)
    return newList

print(squared([6,2,4,1,6,4,9]))

#could put for loop in bracket
def squared2(numList):
    newList = [num**2 for num in numList]
    return newList

print(squared2([6,2,4,1,6,4,9]))

# Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original
# lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
def combinedSum(list1,list2):
    newList = []
    for num1 in list1:
        for num2 in list2:
            if list1.index(num1)==list2.index(num2):
                newList.append(num1+num2)
    return newList

print(combinedSum([1,2,3],[10,20,30]))

# Chapter 10 #10: Count how many words in a list have length 5.
def fiveLetters(stringList):
    five = 0
    for word in stringList:
        count = 0
        for letters in word:
            count = count + 1
        if count >= 5:
            five += 1
    return five

print(fiveLetters(["Hello", "everyone", "my", "name", "is", "Matthew"]))

# Chapter 10 #11: Sum all the elements in a list up to but not including the first even number.
def sumTillEven(numList):
    sum = 0
    for num in numList:
        if(num%2==0):
            return sum
        else:
            sum+=num
    return sum

print(sumTillEven([3,5,7,2,5,6]))

# Chapter 10 #12: Count how many words occur in a list up to and including the first occurrence of the word “sam”.
def sumSam(list):
    count = 0
    for word in list:
        if "sam" in word:
            return count + 1
        else:
            count+=1
    return count

print(sumSam(["Hello", "everyone", "I", "have", "the", "same", "name", "as", "sam"]))