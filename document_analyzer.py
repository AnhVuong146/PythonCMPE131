from collections import Counter

file = open('document.txt', 'r')
readFile = file.read()
list = readFile.split()
dict1 = {}
for t in list:
    if t.lower() in dict1:
        dict1[t.lower()] = dict1[t.lower()] + 1
    else:
        dict1[t.lower()] = 1
sorted_dict = {k:v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse=True)}
count = 1
for key, value in sorted_dict.items():
    print(f' {key} : {value}')
    if count == 5:
        break
    count += 1