import datetime
import random
start_time = datetime.datetime.now()
def disjoint(a,b,c):
    for A in a:
        for B in b:
            for C in c:
                if A==B==C:
                    return False
    return True

n = 1000000
a = [random.randint(1, 100) for _ in range(n)]
b = [random.randint(1, 100) for _ in range(n)]
c = [random.randint(1, 100) for _ in range(n)]

end_time = datetime.datetime.now()
result = disjoint(a, b, c)

print(f"Total run time: {end_time - start_time}")
print(result)