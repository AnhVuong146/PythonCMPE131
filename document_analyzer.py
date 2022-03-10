from collections import Counter

file = open('document.txt', 'r')
readFile = file.read()
list = readFile.split()
d = {}

for i in list:
    words = list
    if i not in d.keys():
        d[i] = 0
    d[i] = d[i] + 1

counts = Counter(words)
top5 = counts.most_common(10)
print(top5)
