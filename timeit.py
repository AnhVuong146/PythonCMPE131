import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        timer()
        end = time.time()
        print("Total time ",end - start)
    return wrapper

def timer():
    time.sleep(2)

function_to_be_used = calculate_time(timer)

function_to_be_used()