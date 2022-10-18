import random

s = open('story.txt')
a = open("adj.txt")
na = open("nounanimal.dat")
nn = open("nounname.dat")
v = open("verbs.dat")
sread = s.read()
aread = a.read()
naread = na.read()
nnread = nn.read()
vread = v.read()
alist = aread.split()
nalist = naread.split()
nnlist = nnread.split()
vlist = vread.split()

def randAdj():
    return alist[random.randrange(len(alist))]

def randNounName():
    return nnlist[random.randrange(len(nnlist))]

def randNounAnimal():
    return nalist[random.randrange(len(nalist))]

def randVerb():
    return vlist[random.randrange(len(vlist))]

def madlibs(story):
    new = sread.split()         # new list of the story
    ind = 0                     # index tracker
    indName = -1                # keeps track if a name is established yet, and what index it is
    for i in new:                                 
        if i == "<NOUNName>":                     # names
            if indName == -1:                     # if this is the first time name is used
                new[ind] = randNounName()         # calls premade random function at index of <NOUNName> (repeated)
                indName = ind                
            else:                                 # else, use the name from the index of first use
                new[ind] = new[indName]
        elif i == "<NOUNAnimal>":                 # animals
            new[ind] = randNounAnimal().lower()
            if(ind == 0 or new[ind-1].find('.')): # if it's the first letter of sentence, capitalize it (repeated)
                new[ind].capitalize()
        elif i == "<VERB>":                       # verbs
            new[ind] = randVerb().lower()
            if(ind == 0 or new[ind-1].find('.')):
                new[ind].capitalize()
        elif i == "<ADJ":                         # adjectives
            new[ind] = randAdj().lower()
            if(ind == 0 or new[ind-1].find('.')):
                new[ind].capitalize()
        ind+=1
    return new.join(' ')                          #turns new list back into a string and returns

print(madlibs(sread))





# previously used stuff
"""
theName = randNounName()

print("On a " +randAdj()+ " and " +randAdj()+ " day, " +theName+" "+randVerb()+ " a " +randAdj()+" "+
randNounAnimal().lower()+". "+theName+ " did not regret it. In fact, "+theName+" did it again the next day. "
+randAdj().capitalize()+" if you ask me. " +randAdj().capitalize()+" is how " +theName+
" used to really be, but now he is just "+randAdj()+ ". I even remember when he "+randVerb()+
" my brother. Unforgivable.")



On a <ADJ> and <ADJ> day, <NOUNName> <PASTVERB> a <ADJ> <NOUNAnimal>. <NOUNName> did not regret it. In fact, 
<NOUNName> did it again the next day. <ADJ> if you ask me. <NOUNName> used to be really <ADJ>, but now he 
is just <ADJ>. I even remember when he <PASTVERB> my brother. Unforgivable.


def randAdj():
    adj = ["bright", "sunny", "gloomy", "dark", "stormy", "yellow", "scary", "plump", "juicy", "cool", "smart"]
    return adj[random.randrange(len(adj))]

def randNounName():
    names = ["Matthew", "Muhammad", "Jose", "Derek", "Thomas", "Evan", "Godzilla", "LeBron"]
    return names[random.randrange(len(names))]

def randNounAnimal():
    names = ["Monkey", "Dolphin", "Owl", "Wooly Mammoth", "Dinosaur", "Hawk", "Worm", "Python"]
    return names[random.randrange(len(names))]

def randVerb():
    verb = ["ate", "threw", "saw", "killed", "married", "smacked", "licked", "tripped", "punted", "helped"]
    return verb[random.randrange(len(verb))]
"""