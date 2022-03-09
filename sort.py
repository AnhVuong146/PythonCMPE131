def sort_list(a):
    if not isinstance(a, list):
        print("Bad Input")
        return[]
    n = len(a)
    temp = 0
    i = 0
    while i < n:
        j = 0
        while j < (n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            j = j + 1
        i = i + 1
    return a

a = [1,3,2,7]
b = [3,2,89,4]
c = [242, 329, 66, 723, 336, 259, 136, 529, 36, 999]
d = ['A', 'E', 'G', 'B', 'H']
e = 3
f = "hello"

print(sort_list(a))
print(sort_list(b))
print(sort_list(c))
print(sort_list(d))
print(*sort_list(e))
print(*sort_list(f))