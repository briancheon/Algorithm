import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
q = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        q.appendleft(int(command[1]))

    elif command[0] == "push_back":
        q.append(int(command[1]))

    elif command[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    
    elif command[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    
    elif command[0] == "size":
        print(len(q))

    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
