import time
def calculate_time(func):
    def wrapper():
        start = time.time()
        temp = func()       
        end = time.time()
        run_time = end - start
        output = ("Total Time " + str(run_time) + "seconds")
        print(output)
        return temp
    return wrapper

@calculate_time
def t1():
    i = 10000000
    while i > 0:
        i -= 1
t1()