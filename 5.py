import datetime
import random
s = [random.randint(10, 100) for _ in range(100000)]
start_time = datetime.datetime.now()
def avg(s):
    n=len(s)
    a=[0]*n
    total=0
    for i in range(100000):
        total+=s[i]
        a[i]=total//(i+1)
       
    return a
print(avg(s))
end_time = datetime.datetime.now()

print(f"Total run time: {end_time - start_time}")