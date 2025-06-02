import sys

def area_sum(arr, x1, y1, x2, y2):
    return (arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])

N, M = map(int, sys.stdin.readline().split())

matrix = [[0] * (M + 1)]
for _ in range(N):
    row = [0] + list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

sum_matrix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
        for j in range(1, M + 1):
            sum_matrix[i][j] = matrix[i][j] + sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1]

K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(area_sum(sum_matrix, x1, y1, x2, y2))