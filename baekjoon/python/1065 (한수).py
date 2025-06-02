import sys

N = int(sys.stdin.readline().rstrip())
count = 0

for i in range(1, N + 1):
    if i // 10 < 10:
        count += 1
    else:
        if int(i // 100) + int((i % 100) % 10) == 2 * int((i // 10) % 10):
            count += 1

print(count)

