import sys

N = int(sys.stdin.readline().rstrip())
dance = {"ChongChong"}

for _ in range(N):
    A, B = sys.stdin.readline().split()
    if A in dance or B in dance:
        dance.add(A)
        dance.add(B)

print(len(dance))
