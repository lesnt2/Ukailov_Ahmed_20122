# 2.1

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