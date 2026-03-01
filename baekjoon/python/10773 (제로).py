import sys

K = int(sys.stdin.readline().rstrip())
q = []

for _ in range(K):
    money = int(sys.stdin.readline().rstrip())
    if money == 0:
        q.pop()
    else:
        q.append(money)

print(sum(q))
