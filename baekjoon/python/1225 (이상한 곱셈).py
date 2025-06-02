import sys

A, B = sys.stdin.readline().split()
A = sum(map(int, list(A)))
B = sum(map(int, list(B)))

print(A * B)
