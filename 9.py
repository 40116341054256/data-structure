
import datetime
import random


a = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1000000000))

start_time = datetime.datetime.now()

def r(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
    return a

reversed_a = r(list(a))  

end_time = datetime.datetime.now()


print(reversed_a)
print(f"Total run time: {end_time - start_time}")

