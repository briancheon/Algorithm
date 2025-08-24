import sys

BASE = 257
MOD  = 10 ** 9 + 7

def row_hash(row, l, r):
    return (row_prefix[row][r] - row_prefix[row][l]*hash[r - l]) % MOD

def col_hash(col, l, r):
    return (col_prefix[col][r] - col_prefix[col][l]*hash[r - l]) % MOD

def solution():
    for m in range(N, 0, -1):
        for p in range(N - m + 1):
            for q in range(N - m + 1):
                if row_hash(p, q, q + m) != row_hash(p + m - 1, q, q + m):
                    continue

                if col_hash(q, p, p + m) != col_hash(q + m - 1, p, p + m):
                    continue

                return p + 1, q + 1, m

N = int(sys.stdin.readline().rstrip())
c = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

hash = [1] * (N + 1)
for i in range(1, N + 1):
    hash[i] = (hash[i - 1] * BASE) % MOD

row_prefix = [[0] * (N + 1) for _ in range(N)]
col_prefix = [[0] * (N + 1) for _ in range(N)]
for i in range(N):
    for j in range(N):
        row_prefix[i][j + 1] = (row_prefix[i][j] * BASE + c[i][j] + 1) % MOD
        col_prefix[j][i + 1] = (col_prefix[j][i] * BASE + c[i][j] + 1) % MOD
        
print(*solution())