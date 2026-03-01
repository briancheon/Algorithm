import sys

S = set()
M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    line = sys.stdin.readline().split()
    if len(line) == 1:
        if line[0] == "all":
            S = set(range(1, 21))
        else:
            S = set()
    else:
        command, n = line[0], int(line[1])
        if command == "add":
            S.add(n)
        elif command == "remove":
            S.discard(n)
        elif command == "check":
            print(1 if n in S else 0)
        elif command == "toggle":
            if n in S:
                S.discard(n)
            else:
                S.add(n)

