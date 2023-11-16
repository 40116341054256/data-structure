import datetime
import random
start_time = datetime.datetime.now()
a = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(100000000))

def r(a):
    n=len(a)
    x=[]*n
    for i in range(n):
        x[n-1-i]=a[i]
    return x
reversed_a = r(list(a)) 
end_time = datetime.datetime.now()
print(reversed_a)
print(f"Total run time: {end_time - start_time}")