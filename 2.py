import datetime

start_time = datetime.datetime.now()
n=100
p=0
for i in range(n):
    i=1
    while i<n:
        k=p
        i*=2
        print(i)
        
end_time = datetime.datetime.now()

print(f"Total run time: {end_time - start_time}")