
list = ["hello",True]      #starting list
list.append("apple")       #append "apple"
list.append(76)            #append 76
list.insert(3,"cat")       #inserts "c" at index 0
list.insert(0,99)          #inserts 99 at index 0
print(list.index("hello")) #index of "hello"
print(list.count(76))      #counts amount of 76
list.remove(76)            #remove first 76 occurence
list.pop(list.index(True)) #remove True with pop & index
print(list)                