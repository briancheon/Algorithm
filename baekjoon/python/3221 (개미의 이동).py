import sys

L, T = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline().rstrip())

ants = []
for _ in range(N):
    pos, dir = sys.stdin.readline().split()
    ants.append((int(pos), dir))

final = []
for pos, dir in ants:
    if dir == "L":
        if pos - T > 0:
            final.append(pos - T)
            
        elif (T - pos) // L % 2:
            final.append(L - (T - pos) % L)
            
        else:
            final.append((T - pos) % L)
    else:
        if pos + T < L:
            final.append(pos + T)
            
        elif (pos + T) // L % 2:
            final.append(L - (pos + T) % L)
            
        else:
            final.append((pos + T) % L)

print(*sorted(final), sep=' ')