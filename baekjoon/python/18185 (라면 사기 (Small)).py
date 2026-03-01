import sys

def cost(ls, idx, num, t):
    diff = min(ls[idx:idx + num])
    ls[idx:idx + num] = map(lambda x: x - diff, ls[idx:idx + num])

    if num == 1:
        return ls, t + 3 * diff
    elif num == 2:
        return ls, t + 5 * diff
    else:
        return ls, t + 7 * diff

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split())) + [0, 0]

total = 0

for c in range(N):
    if A[c + 1] > A[c + 2]:
        n_ramen = min(A[c], A[c + 1] - A[c + 2])
        A[c] -= n_ramen
        A[c + 1] -= n_ramen

        total += 5 * n_ramen
        A, total = cost(A, c, 3, total)

    else:
        A, total = cost(A, c, 3, total)
        A, total = cost(A, c, 2, total)
    A, total = cost(A, c, 1, total)

print(total)
