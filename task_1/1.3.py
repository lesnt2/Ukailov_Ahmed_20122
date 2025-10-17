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