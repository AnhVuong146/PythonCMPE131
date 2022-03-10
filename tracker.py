def func_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1 
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

i = 0
@func_counter
def t1():
    print("Hi")
while (i < 10):
    t1()
    i += 1 

testCount = t1.count
print(testCount)   