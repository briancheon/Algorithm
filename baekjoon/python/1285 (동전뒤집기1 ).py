import sys

N = int(sys.stdin.readline().rstrip())
_coin = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
res = N * N + 1

for bit in range(1 << N):
    tmp = [_coin[i][:] for i in range(N)]
    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'

    tsum = 0
    for i in range(N):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        tsum += min(cnt, N - cnt)
    res = min(res, tsum)
