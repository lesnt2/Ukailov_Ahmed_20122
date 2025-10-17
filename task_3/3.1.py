#3.1
from itertools import combinations

n = int(input())
s = [int(input()) for i in range(n)]
c = int(input())

b_sum = None
b_combo = None
min_d = 100000

for f in combinations(s, 4):
    sum_chis = sum(f)
    d = abs(sum_chis - c)
    if d == 0:
        b_combo = list(f)
        b_sum = sum_chis
        break
    if d < min_d or (d == min_d and sum_chis < b_sum):
        min_d = d
        b_combo = list(f)
        b_sum = sum_chis

print(b_combo)
print(b_sum)