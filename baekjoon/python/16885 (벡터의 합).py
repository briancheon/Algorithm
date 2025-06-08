import sys

def vec_size(a, b):
    x1, y1 = a
    x2, y2 = b

    return (x1 + x2) ** 2 + (y1 + y2) ** 2

def vec_operation(a, b):
    x1, y1 = a
    x2, y2 = b

    if x1 * x2 < 0:
        if y1 * y2 < 0:
            oper = 1, 1
        
        else:
            oper = 1, 3
            y2 *= -1

    else:
        if y1 * y2 < 0:
            oper = 1, 2
            x2 *= -1
        
        else:
            oper = 1, 4
            x2 *= -1
            y2 *= -1

    return vec_size((x1, y1), (x2, y2)), *oper

N = int(sys.stdin.readline().rstrip())
vectors = list(enumerate(tuple(map(int, sys.stdin.readline().split())) for _ in range(N)))
vectors.sort(key=lambda x: (abs(x[1][0]), abs(x[1][1])))

min_size = float('inf')
min_idx, min_oper = None, None
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        sign = 1 if vectors[i][1][0] * vectors[j][1][0] < 0 else -1
        check = (vectors[i][1][0] + vectors[j][1][0] * sign) ** 2
        if check > min_size:
            break
        
        size, oper1, oper2 = vec_operation(vectors[i][1], vectors[j][1])
        if size < min_size:
            min_size = size
            min_idx = (vectors[i][0] + 1, vectors[j][0] + 1)
            min_oper = (oper1, oper2)

print(min_idx[0], min_oper[0], min_idx[1], min_oper[1])