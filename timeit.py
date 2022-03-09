import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        run = end - start
        print(f'Total time: {run}')
    return wrapper

@calculate_time
def test():
    i = 10000000
    while i > 0:
        i -= 1

test()

