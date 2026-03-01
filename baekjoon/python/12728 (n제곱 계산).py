import sys

MOD = 1000

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
    
def n_pow(pow):
    N = [[6,-4],[1,0]]
    result = matrix_pow(N, pow)
    return (result[0][0] + result[1][1] - 1) % MOD

T = int(sys.stdin.readline().rstrip())

for i in range(1, T + 1):
    n = int(sys.stdin.readline().rstrip())
    print(f"Case #{i}: {str(n_pow(n))[-3:].zfill(3)}")
    
