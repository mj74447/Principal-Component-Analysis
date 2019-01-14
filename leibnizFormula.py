#using generators
def odd():
    x=1
    while True:
            yield x
            x = x+2

def pi_series():
    odds = odd()
    approx=0
    while True:
        approx += (4 / next(odds)) 
        yield approx
        approx -= (4/ next(odds))
        yield approx

app_pi = pi_series() 
for x in range(1000):
    print(next(app_pi))       
