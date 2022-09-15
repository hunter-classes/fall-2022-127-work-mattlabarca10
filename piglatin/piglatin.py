def bondify(name):
  result = ""
  location = name.find(' ')
  first = name[0].upper() + name[1:location]
  last = name[location+1].upper() + name[location+2:]
  result = last + ", " + first + " " +last
  return result

print(bondify("Matthew LaBarca"))
print(bondify("james bond"))

def piglatin(word):
  result = ""

  if word[0] in ["a"or"e"or"i"or"o"or"u"or"A"or"E"or"I"or"O"or"U"]:
    result = (word+"yay").lower()
  else:
    result = (word[1:]+word[0]+"ay").lower()
  return result

print(piglatin("Than"))
print(piglatin("apple"))
print(piglatin("Octopus"))
print(piglatin("maTthew"))
print(piglatin("pLuTo"))
