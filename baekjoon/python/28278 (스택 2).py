import sys

N = int(sys.stdin.readline().rstrip())
q = []

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "1":
        q.append(int(command[1]))

    elif command[0] == "2":
        if q:
            print(q.pop())
        else:
            print(-1)

    elif command[0] == "3":
        print(len(q))

    elif command[0] == "4":
        if q:
            print(0)
        else:
            print(1)

    else:
        if q:
            print(q[-1])
        else:
            print(-1)
