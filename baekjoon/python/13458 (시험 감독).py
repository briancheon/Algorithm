import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

minimum = 0
for i in range(N):
    student = A[i] - B
    if student > 0:
        minimum += ((A[i] - B) // C + 1, (A[i] - B) // C)[(A[i] - B) % C == 0]
    minimum += 1

print(minimum)
