import sys

MOD = 1000000007

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_pow(M, p):
    if p == 1:
        return M
    if p % 2 == 0:
        half_pow = matrix_pow(M, p // 2)
        return matrix_mult(half_pow, half_pow)
    else:
        return matrix_mult(M, matrix_pow(M, p - 1))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    Fn, Fm = map(int, sys.stdin.readline().split())
    
    print(fibonacci(gcd(Fn, Fm)) % MOD)