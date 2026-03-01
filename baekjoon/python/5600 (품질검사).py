import sys

a, b, c = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline().rstrip())

parts = [2] * (a + b + c)
normal = set()

info = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
info.sort(key=lambda x: x[3], reverse=True)

for i in range(N):
    if info[i][3] == 1:
        normal.update(info[i][:3])
        x, y, z = info[i][:3]
        parts[x - 1] = 1
        parts[y - 1] = 1
        parts[z - 1] = 1
        
    else: 
        check = list(filter(lambda x: x not in normal, info[i][:3]))
        if len(check) == 1:
            parts[check[0] - 1] = 0

print(*parts, sep='\n')