import timeit
import functools

def calc_values(x,y:int):
    return x+y

n=[1,2,3,4,5]
lo = functools.reduce(calc_values,n)
print(lo)   
print(sum(n))
#what reduce is doing ---->
#result = calc_values(1,2)
#result = calc_values(result,3)
#result = calc_values(result,4)
#result = calc_values(result,5) --> passing final result