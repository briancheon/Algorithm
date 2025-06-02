"""import sys

N = int(sys.stdin.readline().rstrip())

_window = [0] * (N + 1)

for i in range(1, N):
    for j in range(i, N, i):
        _window[j] ^= 1

print(sum(_window))"""

import sys

N = int(sys.stdin.readline().rstrip())

print(int(N ** 0.5))
