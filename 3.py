
import datetime
import random
import string

start_time = datetime.datetime.now()

s = ''.join(random.choices(string.ascii_lowercase, k=1000))

def unique(s):
    for j in range(len(s)):
        for k in range(j+1,len(s)):
            if s[j]==s[k]:
                return False
    return True

print(unique(s))

end_time = datetime.datetime.now()
print(f"Total run time: {end_time - start_time}")
