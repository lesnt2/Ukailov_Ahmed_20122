#4.1
a, b = set(input().split()), set(input().split())

m = a&b

print('1)', len(m), 'элемента:', m)
print('2)', len(a|b) - len(m), 'элементов:', a.union(b) - m)
print('3)', len(a-b), 'элементов:', a-b)
print('4)', len(b-a), 'элементов:', b-a)