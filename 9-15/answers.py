#7
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
   
print(is_even(10))
print(is_even(5))

#8
def is_odd(n):
    if n%2 == 1:
        return True
    else:
        return False
   
print(is_odd(10))
print(is_odd(5)

#10
#syntax works fine in thonny for line below
def is_rightangle(a,b,c): 
    rightangle = False
    if abs(b**2 + a**2 - c**2) < 0.001:    \
        rightangle = True
    return rightangle

print (is_rightangle(3,4,5))
print (is_rightangle(3,4,6))
      
#11
def is_rightangle2(a,b,c):
    rightangle = False

    if a > b and a > c and abs(b**2 + c**2 - a**2) < 0.001:
        rightangle = True
    elif b > a and b > c and abs(a**2 + c**2 - b**2) < 0.001:
        rightangle = True
    elif c > a and c > b and abs(a**2 + b**2 - c**2) < 0.001:
        rightangle = True
    
    return rightangle
        

print (is_rightangle2(5,4,3))
print (is_rightangle2(7,4,6))

#hello_name
def hello_name(name):
  return "Hello "+name+"!"

#make_out_word
def make_out_word(out, word):
  return out[0:2]+word+out[2:4]

#first_two
def first_two(str):
  return str[0:2]