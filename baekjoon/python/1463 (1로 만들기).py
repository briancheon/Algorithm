import sys
from queue import Queue

N = int(sys.stdin.readline().rstrip())

q = Queue()
count = 0

q.put((N, 0))
visited = {N}

while q:
    n, count = q.get()
    if n == 1:
        break
    if n % 3 == 0 and n // 3 not in visited:
        q.put((n // 3, count + 1))
        visited.add(n // 3)

    if n % 2 == 0 and n // 2 not in visited:
        q.put((n // 2, count + 1))
        visited.add(n // 2)

    if n - 1 not in visited:
        q.put((n - 1, count + 1))
        visited.add(n - 1)

print(count)
