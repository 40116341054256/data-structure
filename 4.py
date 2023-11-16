
import datetime
import random

start_time = datetime.datetime.now()

s = [random.randint(10, 100) for _ in range(10000)]

def avg(s):
    n = len(s)
    a = [0] * n
    for j in range(10000):
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[i] = total // (j + 1)
    return a

print(avg(s))

end_time = datetime.datetime.now()
print(f"Total run time: {end_time - start_time}")
