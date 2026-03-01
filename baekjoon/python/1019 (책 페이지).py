import sys

N = int(sys.stdin.readline().rstrip())
num_count = [0] * 10

i = 1
extra = 0
while N > 0:
    cur = N % 10
    N //= 10

    num_count[0] -= i
    num_count[cur] += N * i + 1 + extra

    for j in range(10):
        if j == cur:
            continue
        num_count[j] += (N + (0, 1)[j < cur]) * i

    extra += cur * i
    i *= 10

print(*num_count)
