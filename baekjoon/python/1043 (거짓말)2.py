import sys

N, M = map(int, sys.stdin.readline().split())

truth = set(list(map(int, sys.stdin.readline().split()))[1:])

parties = [set(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(M)]

for _ in range(M):
    for party in parties:
        if len(truth & party) > 0:
            truth |= set(party)

cnt = 0
for party in parties:
    if len(party & truth) == 0:
        cnt += 1

print(cnt)