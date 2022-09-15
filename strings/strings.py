s1 = "Hello World"
s2 = 'another\nstring'
s3 = """
Multiline
String
"""
s4 = s1+s1
print(s4)
print(s1*3)
print(3*s1)

print(len(s1))
print(len("abcde"))

# look for string functions

def initialize(name):
  result = ""
  first = name[0].upper()
  location = name.find(' ')
  last = name[location+1].upper() +name[location+2:]
  result = result + first + ". " +last
  return result
  #return name[0].upper() + ". "+ name[name.find(" "):(name.len()-1)]

print(initialize("James Bond"))
 
def bondify(name):
  result = ""
  location = name.find(' ')
  first = name[0].upper() + name[1:location]
  last = name[location+1].upper() + name[location+2:]
  result = last + ", " + first + " " +last
  return result

print(bondify("Matt LaBarca"))
