#Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.
#Exercise 10.4

def average(numlist):
  tot = 0
  for num in numlist:
    tot = tot + num
  return tot / len(numlist)

print(average([2,3,4]))
  
#Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
#Exercise 10.6

def sum_of_squares(xs):
  tot = 0
  for num in xs:
    tot = tot + (num**2)
  return tot

print(sum_of_squares([2,3,4]))