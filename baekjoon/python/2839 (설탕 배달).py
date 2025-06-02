import sys

N = int(sys.stdin.readline().rstrip())

x = N // 5
min_count = float('inf')
success = False

for c in range(x + 1):
    N_temp = N - 5 * c
    if N_temp % 3 == 0:
        count = c + N_temp // 3
        if count < min_count:
            min_count = count
            success = True

if success:
    print(min_count)
else:
    print(-1)
