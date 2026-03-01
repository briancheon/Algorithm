import sys

N = int(sys.stdin.readline().rstrip())

relationships = {i: list(sys.stdin.readline().rstrip()) for i in range(1, N + 1)}
relation_count = [0] * N

for person, relationship in relationships.items():
    for i in range(N):
        if relationship[i] == "Y" or relationships[i + 1][person - 1] == "Y":
            ...
    