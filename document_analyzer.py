from collections import Counter

def document_analyzer():
    d = {}
    list = []
    frequencies = Counter()
    with open('document.txt') as file:
        for line in file:
            frequencies.update(line.split())
    print(frequencies)   
    
    most_frequent = sorted(frequencies.most_common(5), key=lambda x: (-x[1], x[0]))
    print()
    for (word, count) in most_frequent:
        print(f'{word}: {count}')
    
document_analyzer()
