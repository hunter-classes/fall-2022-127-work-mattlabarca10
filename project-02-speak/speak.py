pirate = open('pirate.dat').read()       # opens and reads all files    
inp = open('input.txt').read()
input = inp.lower().split()
psplit = pirate.split('\n')
piratespeak = {}
for word in psplit:
    piratespeak.update({word[:word.index(":")]:word[word.index(':')+1:]})
keys = []
for word in psplit:
    keys.append(word[:word.index(":")])
npinput = []
for word in input:
    if ',' in word or '.' in word or '!' in word:
        npinput.append(word[:-1])
    else:
        npinput.append(word)

newstory = []
ind = 0
for word in npinput:                                 
    if word in keys: 
        newstory.append(piratespeak[word])
    elif word == "<surprise>":
        newstory.append("Blow me down!")
    elif word == "<drinkwithcrew>":
        newstory.append("Splice the mainbrace!")
    else:
        newstory.append(word)  
    if ind == 0 or word == 'i' or '.' in input[ind-1] or '!' in input[ind-1]:
        newstory[ind] = newstory[ind].capitalize() 
    if "." in input[ind]:
        newstory[ind] = newstory[ind] + "."
    elif "," in input[ind]:
        newstory[ind] = newstory[ind] + ","
    elif "!" in input[ind]:
        newstory[ind] = newstory[ind] + "!"
    ind+=1
final = ' '.join(newstory)

print(input)
print(final)


