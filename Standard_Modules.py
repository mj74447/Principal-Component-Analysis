import sys
import os
import random
import datetime
def main():
    v = sys.version_info
    x = sys.platform
    print('python version {}.{}.{}'.format(*v))#current version
    print(x)#platform in case of windows- win32
    y = os.name
    print(y)#unix varient will be returned
    path_get = os.getenv('PATH')
    print(path_get)
    #getting my current Working directory
    get_current_working_direc = os.getcwd()
    print('\n'+get_current_working_direc)
    random_no = os.urandom(25)# a random function from os 25 bytes long
    print(random_no)
    #changing it into hexadecimal
    hex_n=random_no.hex()
    print(hex_n)
    #------------------working with random module-----------------------------------------
    x = random.randint(1,100)
    print(x)
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    #---------------working with datetime module--------------------------------------------
    x_now = datetime.datetime.now()
    print(x_now.year,x_now.day,x_now.month,x_now.hour,x_now.min,x_now.second,x_now.microsecond)
    
if __name__ == '__main__':
    main()
