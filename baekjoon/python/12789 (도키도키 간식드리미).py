import sys

N = int(sys.stdin.readline().rstrip())

order = list(map(int, sys.stdin.readline().split()))
q = []
num = 1

for o in order:
    q.append(o)
    while q and q[-1] == num:
        q.pop()
        num += 1

if q:
    print("Sad")
else:
    print("Nice")
