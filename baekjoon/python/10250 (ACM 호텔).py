import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    X, Y = (N // H, N // H + 1)[N % H != 0], (N % H, H)[N % H == 0]
    print(f'{Y}{(X, "0" + str(X))[X // 10 == 0]}')

