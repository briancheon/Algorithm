import sys

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

def union(node1, node2):
    n1 = find(node1)
    n2 = find(node2)
    
    if n1 < n2:
        parent[n2] = n1

    else:
        parent[n1] = n2

N, M = map(int, sys.stdin.readline().split())
truth = list(map(int, sys.stdin.readline().split()))[1:]

parent = list(range(N + 1))

for person in truth:
    union(0, person)  # 진실을 아는 사람의 부모를 0으로 설정

parties = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(M)]

for party in parties:
    for i in range(1, len(party)):
        union(party[i], party[i - 1])

cnt = 0
for party in parties:
    if find(party[0]) != 0:
        cnt += 1

print(cnt)
