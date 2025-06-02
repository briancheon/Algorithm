import sys

N = sys.stdin.readline().rstrip()

print(''.join(sorted(N, reverse=True)))
