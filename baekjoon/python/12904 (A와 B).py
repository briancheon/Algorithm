import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

while len(T) > len(S):
    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1][::-1]

if S == T:
    print(1)
else:
    print(0)
