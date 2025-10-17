#3.3
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