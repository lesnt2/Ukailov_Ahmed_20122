#Task_1
# 1.1
```
a = int(input())
b = str(a)  #меняется число в строку и присвыевается b
x = str(a)  #меняется число в строку и присвыевается x
x = x[::-1] #строка разворачивается 
if x == b:  
    print('True')
else:
    print('False')

```
# 1.2
```
a = int(input())
if not((-2**7) <= a <= (2**7-1)):  #проверяется подходит ли число по диапазонеу
    print('no solution')
if a < 0:      #если число отрицательное 
    b = int('-' + (str(abs(a))[::-1])) #переварачиваем число и дописываеми '-'
    if b < (-2**7): # опять проверка в диапазоне 
        print('no solution')
    else:
        print(b)
else:   # если чило не отрицательное
    b = int(str(a)[::-1])  #переворачиваем его и ниже проверяем 
    if b > (2**7-1):
        print('no solution')
    else:
        print(b)
```
#1.3
```
d = [input(), int(input())]
s = d[0]
x = d[1]

if x == 1:
    print(s)
else:
    f = ''
    n = len(s)
    y = 2 * x - 2
    
    for i in range(x):
        for j in range(i, n, y):
            f += s[j]
            if i != 0 and i != x - 1 and (j + y - 2) * i < n:
                f += s[(j + y - 2) * i]
    print(f)
```

#Task_2
# 2.1
```
s = input()
y = ''
m = []

if len(s) == len(set(s)):
    print(s)
else:
    for i in range(len(s)):  #создаем левую и правую границу
        for x in range(i, len(s)):
            v = s[i:x] #берём срез по этим границам
            if len(v) == len(set(v)): #проверка что все буквы различны
                m.append(v) #добовляем во множесто m

    for i in m:
        if len(y) < len(i): #присваеваем значению y самый длинный отрезок
            y = i
    print(y)
```
#2.2
```
s = input() #вводим текст
b = s.split() #разделяем по побелам слова
b.reverse()  #меняем местами слова 
r = ' '.join(b)  #соединяем их в строку 
print(r.capitalize()) #выводим с правильным регистром
```

#Task_3
#3.1
```
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
```
#3.2
```
from itertools import *
a = input()
s = list(a)
m = []
for i in permutations(s):
    m.append(i)
print(m)
```
#3.3
```
a = input()
a = a.split()
m = []
s = []
for l in range(len(a)):
    for r in range(l+1, len(a)-1):
        if sorted(a[l]) == sorted(a[r]) and a[l] != a[r]:
            s.append(a[l])
            s.append(a[r])
            m.append(s)
            s = []
for i in range(len(m)):
    for g in range(2):
        a.remove(m[i][g])
for i in range(len(a)):
    s.append(a[i])
    m.append(s)
    s = []
print(m)
```

#Task_4
#4.1
```
a, b = set(input().split()), set(input().split())

m = a&b

print('1)', len(m), 'элемента:', m)
print('2)', len(a|b) - len(m), 'элементов:', a.union(b) - m)
print('3)', len(a-b), 'элементов:', a-b)
print('4)', len(b-a), 'элементов:', b-a)
```

#4.2
```
from itertools import *

a = set(input().split())

s = []
for i in range(1, len(a) + 1):
    for f in combinations(a, i):
        s.append(set(f))
print(s)     
print(len(s))
```

#Task_5
#5.1
```
matrix = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

def spiral_order(m):
    r = []
    while m:
        r.extend(m[0])
        m = list(zip(*m[1:]))[::-1]
    return r

result = spiral_order([row[:] for row in matrix])
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

