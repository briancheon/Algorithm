import sys

n = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().split()))

ans = 0

while True:
    if len(L) == 1:
        break
    
    maximum = max(L)
    max_idx = L.index(maximum)

    if 0 < max_idx < len(L) - 1:
        max_next = max(L[max_idx - 1], L[max_idx + 1])

    elif max_idx == 0:
        max_next = L[max_idx + 1]

    else:
        max_next = L[max_idx - 1]

    ans += maximum + max_next
    L.remove(max_next)

print(ans)