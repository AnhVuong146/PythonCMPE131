import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        temp = func()       
        end = time.time()
        run = end - start
        output = (f"Total Time {run}seconds")
        print(output)
        return temp
    return wrapper

@calculate_time
def t1():
    i = 10000000
    while i > 0:
        i -= 1
t1()