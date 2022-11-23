person = {'first' : 'John', 'last': 'Smith', 'age': 50}

k = person.keys()
i = person.items()
print(person.setdefault('age'))
print(k)
print(i)

for k in person.keys():
    print(k,person[k])

def count_letters():
    counts = {}
    for letter in s:
        if letter in counts.keys():
            counts[letter] = counts[letter]+1
        else:
            counts[letter] = 1
    return counts
    