import sys

def cost(b, c, ls, idx, num, t):
    diff = min(ls[idx:idx + num])
    ls[idx:idx + num] = map(lambda x: x - diff, ls[idx:idx + num])

    if num == 1:
        return ls, t + b * diff
    elif num == 2:
        return ls, t + (b + c) * diff
    else:
        return ls, t + (b + 2 * c) * diff

N, B, C = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split())) + [0, 0]

if B > C:
    total = 0

    for i in range(N):
        if A[i + 1] > A[i + 2]:
            n_ramen = min(A[i], A[i + 1] - A[i + 2])
            A[i] -= n_ramen
            A[i + 1] -= n_ramen

            total += (B + C) * n_ramen
            A, total = cost(B, C, A, i, 3, total)

        else:
            A, total = cost(B, C, A, i, 3, total)
            A, total = cost(B, C, A, i, 2, total)
        A, total = cost(B, C, A, i, 1, total)

    print(total)

else:
    print(sum(A) * B)
