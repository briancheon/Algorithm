"""
G(0) ~ G(100)
0 0 1 0 2 1 3 0 4 2 5 1 6 3 7 0 8 4 9 2 10 5 11 1 12 6 13 3 14 7 15 0 16 8 17 4 18 9 19 2 20 10 21 5 22 11 23 1 24 12 25 6 26 13 27 3 28 14 29 7 30 15 31 0 32 16 33 8 34 17 35 4 36 18 37 9 38 19 39 2 40 20 41 10 42 21 43 5 44 22 45 11 46 23 47 1 48 24 49 12 50

G(2n + 0) : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50

G(4n + 1) : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

G(8n + 3) : 0 1 2 3 4 5 6 7 8 9 10 11 12

G(16n + 7) : 0 1 2 3 4 5

G(32n + 15) : 0 1 2

G(64n + 31) : 0 1

G(128n + 63) : 0
"""

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().split()))

    nim_sum = 0
    for ai in a:
        p = 1
        while 2 ** p <= ai:
            if ai % (2 ** p) == 2 ** (p - 1) - 1:
                break
            p += 1

        Ga = ai // (2 ** p)
        nim_sum ^= Ga

    print("YES" if nim_sum else "NO")