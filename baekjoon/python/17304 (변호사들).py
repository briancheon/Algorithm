import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(set)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].add(A)

for lawyer in range(1, N + 1):
    if lawyer not in graph:
        graph[lawyer] = set()

if all(len(defenders) >= 2 for defenders in graph.values()):
    print("YES")

else:
    stack = [lawyer for lawyer, defenders in graph.items() if len(defenders) == 1]
    visited = set(stack)
    
    while stack:
        cur = stack.pop()
        defender = next(iter(graph[cur]))
        
        graph[defender].discard(cur)
        
        if defender not in visited and len(graph[defender]) == 1:
            stack.append(defender)
            visited.add(defender)

        elif len(graph[defender]) == 0:
            break

    if any(len(defenders) == 0 for defenders in graph.values()):
        print("NO")

    else:
        print("YES")