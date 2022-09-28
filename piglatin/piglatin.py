"""
def bondify(name):
  result = ""
  location = name.find(' ')
  first = name[0].upper() + name[1:location]
  last = name[location+1].upper() + name[location+2:]
  result = last + ", " + first + " " +last
  return result

print(bondify("Matthew LaBarca"))
print(bondify("james bond"))
"""

def piglatin(word):
  result = ""
  first = word[0]
  first = str(first)
  last = word[len(word)-1]
  last = str(last)
  punc = False
  if last in '.!?,':
     punc = True
  a = len(word)-1
  if (punc == True):     
    if first in 'aeiouAEIOU':
      result = (word[0:a]+"yay"+last).lower()
    else:
      result = (word[1:a]+word[0]+"ay"+last).lower()
  else: 
    if first in 'aeiouAEIOU':
      result = (word[0:]+"yay").lower()
    else:
      result = (word[1:]+word[0]+"ay").lower()
  
  return result

print(piglatin("Family."))
print(piglatin("Than!"))
print(piglatin("apple,"))
print(piglatin("Octopus"))
print(piglatin("maTthew?"))
print(piglatin("You're"))
