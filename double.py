def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper

@doubler
def idk():
    print('hi')

idk()