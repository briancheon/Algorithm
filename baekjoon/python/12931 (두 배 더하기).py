import sys

N = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))

count = 0

while sum(B) > 0:
    if all(i % 2 == 0 for i in B):
        B = list(map(lambda x: x // 2, B))
        count += 1
    else:
        for c in range(len(B)):
            if B[c] % 2 != 0:
                B[c] -= 1
                count += 1

print(count)
