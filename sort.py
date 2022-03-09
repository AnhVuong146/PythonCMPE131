a = [1,3,2,7]
b = [3,2,4,89]
c = 3
d = "hello"

def sort_list(a):
    if not isinstance(a, list):
        print("Bad Input")
        return[]
    n = len(a)
    temp = 0
    i = 0
    j = 0
    while i < n:
        while j < (n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            j = j + 1
        i = i + 1
    return a

print(sort_list(a))
print(sort_list(b))
print(*sort_list(c))
print(*sort_list(d))

