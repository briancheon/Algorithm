import sys
from queue import Queue

N, M = map(int, sys.stdin.readline().split())

in_degree = [0] * N
graph = [[] for _ in range(N)]

for i in range(M):
    singers = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))[1:]
    for j in range(len(singers) - 1):
        graph[singers[j]].append(singers[j + 1])
        in_degree[singers[j + 1]] += 1


def topology_sort():
    result = []
    q = Queue()

    for c in range(N):
        if in_degree[c] == 0:
            q.put(c)

