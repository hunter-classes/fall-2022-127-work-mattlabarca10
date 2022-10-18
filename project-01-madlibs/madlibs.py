import random

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
 
theName = randNounName()

print("On a " +randAdj()+ " and " +randAdj()+ " day, " +theName+" "+randVerb()+ " a " +randAdj()+" "+
randNounAnimal().lower()+". "+theName+ " did not regret it. In fact, "+theName+" did it again the next day. "
+randAdj().capitalize()+" if you ask me. " +randAdj().capitalize()+" is how " +theName+
" used to really be, but now he is just "+randAdj()+ ". I even remember when he "+randVerb()+
" my brother. Unforgivable.")


"""
On a <ADJ> and <ADJ> day, <NOUNName> <PASTVERB> a <ADJ> <NOUNAnimal>. <NOUNName> did not regret it. In fact, 
<NOUNName> did it again the next day. <ADJ> if you ask me. <NOUNName> used to be really <ADJ>, but now he 
is just <ADJ>. I even remember when he <PASTVERB> my brother. Unforgivable.
"""