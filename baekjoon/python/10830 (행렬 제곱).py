import sys

MOD = 1000


def matrix_mult(A, B):
    result = [[0] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD
             
    return result


def matrix_pow(M, p):
    if p == 1:
        return M
    if p % 2 == 0:
        half_pow = matrix_pow(M, p // 2)
        return matrix_mult(half_pow, half_pow)
    else:
        return matrix_mult(M, matrix_pow(M, p - 1))


N, B = map(int, sys.stdin.readline().split())
matrix = [[*map(lambda x: int(x) % MOD, sys.stdin.readline().split())] for _ in range(N)]

answer = matrix_pow(matrix, B)
for row in answer:
    print(*row)