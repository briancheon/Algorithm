import sys

a, b = map(lambda x: int(x[::-1]), sys.stdin.readline().split())
print(max(a, b))
