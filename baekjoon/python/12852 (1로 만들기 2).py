import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

q = deque()
q.append((N, 0, [N]))
visited = {N}

while q:
    n, count, ops = q.popleft()
    if n == 1:
        print(count)
        print(*ops)
        exit()
        
    n_div_3 = n // 3
    n_div_2 = n // 2
    if not n % 3 and n_div_3 not in visited:
        visited.add(n_div_3)
        q.append((n_div_3, count + 1, ops + [n_div_3]))
    if not n % 2 and n_div_2 not in visited:
        visited.add(n_div_2)
        q.append((n_div_2, count + 1, ops + [n_div_2]))
    if n - 1 not in visited:
        visited.add(n - 1)
        q.append((n - 1, count + 1, ops + [n - 1]))
