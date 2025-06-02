import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip())
a = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

nim_sum = reduce(lambda x, y: x ^ y, a)

if nim_sum == 0:
    print("Alice" if any(ai % 2 for ai in a) else "Bob")

else:
    print("Bob" if nim_sum == 1 else "Alice")