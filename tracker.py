def func_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1 
        return func(*args, **kwargs)

    wrapper.counter = 0
    return wrapper

@func_counter
def t1():
    print("Hi")

x = 0
while (x < 10):
    t1()
    x += 1

testCount = t1.counter
print(testCount)   