#4.2
from itertools import *

a = set(input().split())

s = []
for i in range(1, len(a) + 1):
    for f in combinations(a, i):
        s.append(set(f))
print(s)     
print(len(s))