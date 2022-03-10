from collections import Counter

file = open('document.txt', 'r')
readFile = file.read()
list = readFile.split()
d = {}

for i in list:
    if i not in d.keys():
        d[i] = 0
    d[i] = d[i] + 1

sorted_d = {k:v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

counts = Counter(list)
top5 = counts.most_common(5)
count = 1
for top5, counts in sorted_d.items():
    print(f'{top5}: {counts}')
    if count == 5:
        break
    count += 1

