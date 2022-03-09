import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        a = func()
        end = time.time()
        run = end - start
        print(f'Total time {run}')
        return a
    return wrapper

@calculate_time
def t1():
    i = 10000000
    while i > 0:
        i -= 1

t1()

