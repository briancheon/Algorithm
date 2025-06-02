import sys
from queue import Queue

def minimum(target):
    q = Queue()
    q.put((1, 0, []))
    possible = [1]

    while q:
        num, count, op = q.get()
        if num == target:
            return count, op

        check = list(map(lambda x: num + x, possible))

        for i in check:
            if i <= target and i not in possible:
                q.put((i, count + 1, op + [i - num]))
                possible.append(i)

            elif i > target:
                break

T = int(sys.stdin.readline().rstrip())

for c in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(minimum(N))
