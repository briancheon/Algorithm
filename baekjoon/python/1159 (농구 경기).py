import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
players = defaultdict(int)

for _ in range(N):
    players[sys.stdin.readline().rstrip()[0]] += 1

selection = sorted(map(lambda x: x[0], filter(lambda x: x[1] >= 5, players.items())))
if not selection:
    print("PREDAJA")
else:
    print(''.join(selection))
