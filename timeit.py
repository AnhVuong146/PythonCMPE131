import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        temp = func()       
        end = time.time()
        run = end - start
        print(f"Total Time {run}seconds")
        return temp
    return wrapper

@calculate_time
def function():
    i = 10000000
    while i > 0:
        i -= 1
function()