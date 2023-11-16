
import datetime
import random

def disjoint(a, b, c):
    for A in a:
        for B in b:
            if A == B:
                for C in c:
                    if A == C:
                        return False
    return True

n = 10000000
a = [random.randint(1, 100) for _ in range(n)]
b = [random.randint(1, 100) for _ in range(n)]
c = [random.randint(1, 100) for _ in range(n)]

start_time = datetime.datetime.now()

result = disjoint(a, b, c)

end_time = datetime.datetime.now()

print(f"Total run time: {end_time - start_time}")
print(result)
