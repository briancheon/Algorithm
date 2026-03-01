import sys

def d(x, y):
    return min(abs(x - y), 1 - abs(x - y))


def f(a):
    min_d = float('inf')
    total_d = 0
    for i in range(1, N):
        dist = d(a[i], a[i - 1])
        total_d += dist
        if dist < min_d:
            min_d = dist
    
    return total_d, min_d


N = int(sys.stdin.readline().rstrip())
A = list(map(lambda x: int(x.split('/')[0]) / int(x.split('/')[1]), sys.stdin.readline().split()))

f_A = f(A)
if f_A * N / (N - 1) < A[-1] - A[0]:
    print('YES')
else:
    print('NO')

