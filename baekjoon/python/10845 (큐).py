import sys

class Queue:
    def __init__(self):
        self.q = []

    def popleft(self):
        return self.q.pop(0)

    def push(self, x):
        self.q.append(x)

    def size(self):
        return len(self.q)

    def front(self):
        return self.q[0]

    def back(self):
        return self.q[-1]

N = int(sys.stdin.readline().rstrip())
queue = Queue()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        queue.push(int(command[1]))

    elif command[0] == "pop":
        if queue.q:
            print(queue.popleft())
        else:
            print(-1)

    elif command[0] == "size":
        print(queue.size())

    elif command[0] == "empty":
        if queue.q:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if queue.q:
            print(queue.front())
        else:
            print(-1)

    else:
        if queue.q:
            print(queue.back())
        else:
            print(-1)
