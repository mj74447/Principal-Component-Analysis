import sys

def my_rangeFunc(n: int):
    start = 0
    while start < n:
        yield start
        start +=1

#x = range(10000)
x = my_rangeFunc(6) 
print("Range  is  {} bytes".format(sys.getsizeof(x)))
#both x and l are iterators but they have huge difference in sizes
#creating a list containing values in x
l = []
for _ in x :
    l.append(_)
    
print("big list is {} bytes".format(sys.getsizeof(l)))
print(x)
print(l)


