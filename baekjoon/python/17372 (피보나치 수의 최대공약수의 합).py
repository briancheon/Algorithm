import sys

MOD = 1_000_000_007
MAX = 1000000

memo = {}
def S(x):
    if x < MAX:
        return phi[x]

    if x in memo:
        return memo[x]
    ret = x * (x + 1) // 2
    i = 2
    while i <= x:
        j = x // (x // i)
        ret -= (j - i + 1) * S(x // i)
        i = j + 1
    memo[x] = ret
    return ret

def product_mat(A, B):
    return [
        [
            (A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0]) % MOD,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1]) % MOD,
            (A[0][0]*B[0][2] + A[0][1]*B[1][2] + A[0][2]*B[2][2]) % MOD,
        ],
        [
            (A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0]) % MOD,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1]) % MOD,
            (A[1][0]*B[0][2] + A[1][1]*B[1][2] + A[1][2]*B[2][2]) % MOD,
        ],
        [
            (A[2][0]*B[0][0] + A[2][1]*B[1][0] + A[2][2]*B[2][0]) % MOD,
            (A[2][0]*B[0][1] + A[2][1]*B[1][1] + A[2][2]*B[2][1]) % MOD,
            (A[2][0]*B[0][2] + A[2][1]*B[1][2] + A[2][2]*B[2][2]) % MOD,
        ]
    ]

def matrix_pow(mat, exp):
    result = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    while exp > 0:
        if exp % 2 == 1:
            result = product_mat(result, mat)
        mat = product_mat(mat, mat)
        exp //= 2
    
    return result

def getFibonacciSum(x):
    if x <= 2:
        return x

    base = [
        [2, 0, -1],
        [1, 0,  0],
        [0, 1,  0]
    ]

    M = matrix_pow(base, x - 3)
    ret = (M[0][0] * 4 + M[0][1] * 2 + M[0][2]) % MOD
    return ret

def solve(x):
    ans = (2 * S(x) - 1) % MOD
    i = 2
    la = 1

    while i <= x:
        pre = la
        la = x // (x // i)
        term = (getFibonacciSum(la) - getFibonacciSum(pre)) % MOD
        ans = (ans + term * (2 * S(x // i) - 1)) % MOD
        i = la + 1

    return ans % MOD

n = int(sys.stdin.readline().rstrip())

phi = [0] * MAX
for i in range(1, MAX):
    phi[i] += i
    j = 2
    while j * i < MAX:
        phi[j * i] -= phi[i]
        j += 1
    phi[i] += phi[i - 1]

print(solve(n))
