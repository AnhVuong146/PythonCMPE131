import time

def calculate_time():
    start = time.time()
    time.sleep(2)

    end = time.time()

    print("Total time" ,end - start)

calculate_time()