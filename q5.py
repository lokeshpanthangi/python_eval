import time as t

def normal():
    sus = 0
    for i in range(1,10000000):
        sus  += i**2
    return sus

async def multi():
    for i in range(1,1000000000):
        sus += i**2
    return sus

print(normal,multi)