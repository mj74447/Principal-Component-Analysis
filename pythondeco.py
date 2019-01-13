
def log(f):
    def logged(x,y):
        rv = f(x,y)
        print(f.__name__,x,y,'->',rv)
        return rv
    return logged    

@log# nothing but--add = log(add)
 
def add(x,y=10):
    ''' add two things'''
    return x+y
print('1 + 2 = ', add(1,2))
print('10 + 20 =', add(10, 20))
