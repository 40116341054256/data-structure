import datetime

start_time = datetime.datetime.now()

def f(x,y,n):
    
    if x>y:
        for i in range(n):
            print(i)
    else:
        for i in range(n):
            for j in range(n):
                print(i,j)

f(2,4,10)

end_time = datetime.datetime.now()

print(f"Total run time: {end_time - start_time}")
hello