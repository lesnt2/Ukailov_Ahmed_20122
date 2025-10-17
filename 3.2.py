# #3.2
from itertools import *
a = input()
s = list(a)
m = []
for i in permutations(s):
    m.append(i)
print(m)