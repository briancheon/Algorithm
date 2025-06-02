import sys

m, a, c, X0, n, g = map(int, sys.stdin.readline().split())

def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m]
    ]

def matrix_pow(M, p):
    if p == 1:
        return M
    
    if p % 2 == 0:
        half_pow = matrix_pow(M, p // 2)
        return matrix_mult(half_pow, half_pow)
    
    return matrix_mult(M, matrix_pow(M, p - 1))

def X(x0, a, c, n):
    if n == 1:
        return x0
    base = [[x0, 1], [0, 0]]
    mul = [[a, 0], [c, 1]]
    result = matrix_mult(base, matrix_pow(mul, n))
    return result[0][0]

print(X(X0, a, c, n) % g)