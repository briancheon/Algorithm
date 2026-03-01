import sys
import heapq

def dijkstra(g, start):
    distances = {node: float('inf') for node in g}
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        current_distance, current_destination = heapq.heappop(q)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in g[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])

    return distances


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().rstrip())

graph = {i: {} for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if u not in graph or v not in graph[u] or w < graph[u][v]:
        graph[u][v] = w

dist_data = dijkstra(graph, K)
for node, dist in dist_data.items():
    print("INF" if dist == float('inf') else dist)
