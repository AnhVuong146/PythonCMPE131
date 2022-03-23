#Anh Vuong
#minMax Method
'''write a function named minmax with a while loop to go through 
a list named stocks and return two numbers: the min and max of the list
see example.
#output would be the numbers in the comment below
print(minmax([10,-5,100,8,36]))
'''

def minMax(stocks):
    n = len(stocks)
    max = stocks[0]
    min = stocks[0]
    i=0
    while(i < n):
        if stocks[i] > max:
            max = stocks[i] 
        elif stocks[i] < min:
            min = stocks[i]
        i += 1
    return min,max

print(minMax([10,-5,100,8,36]))