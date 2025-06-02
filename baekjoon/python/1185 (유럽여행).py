import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, P = map(int, sys.stdin.readline().split())

parent = [i for i in range(N + 1)]

edges = []
total_cost = 0

costs = [float('inf')] + [int(sys.stdin.readline().rstrip()) for _ in range(N)]
min_cost = min(costs[1:])

for _ in range(P):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost * 2 + costs[a] + costs[b], a, b))

edges.sort()

for i in range(P):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost + min_cost)