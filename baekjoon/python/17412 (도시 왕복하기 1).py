import sys
from queue import Queue

INF = float('inf')

def possible(start, end, visited):
    global cities
    q = Queue()
    q.put(start)

    while q and not visited[end]:
        cur = q.get()

        for city in cities[cur]:
            if capacity[cur][city] - current_flow[cur][city] > 0 and not visited[city]:
                q.put(city)
                visited[city] += 1

                if city == end:
                    break

    if not visited[end]:
        return True

    return False


N, P = map(int, sys.stdin.readline().split())

cities = [[] * N for _ in range(N)]
capacity = [[0] * N for _ in range(N)]
current_flow = [[0] * N for _ in range(N)]

for c in range(P):
    start_city, end_city = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    cities[start_city].append(end_city)
    cities[end_city].append(start_city)

    capacity[start_city][end_city] = 1

while True:

    if not possible()
