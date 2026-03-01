import sys

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
C = list(map(int, sys.stdin.readline().split()))

answer = []

for i in range(N):
    if A[i] == 0:
        answer.append(B[i])

answer = answer[::-1]
answer += C

print(*answer[:M])
