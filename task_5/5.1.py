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