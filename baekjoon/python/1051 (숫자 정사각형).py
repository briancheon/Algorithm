import sys

def max_square(n, m, arr):
    max_size = 0
    for i in range(n):
        for j in range(m):
            for k in range(min(n - i, m - j)):
                if arr[i][j] == arr[i + k][j] == arr[i][j + k] == arr[i + k][j + k]:
                    if k + 1 > max_size:
                        max_size = k + 1
    return max_size ** 2


N, M = map(int, sys.stdin.readline().split())

rectangle = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

print(max_square(N, M, rectangle))
