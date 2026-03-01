import sys

def VPS(ps):
    q = []
    for s in ps:
        if s == "(":
            q.append(s)
        else:
            try:
                q.pop()
            except IndexError:
                return "NO"
    return "NO" if q else "YES"

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    PS = sys.stdin.readline().rstrip()
    print(VPS(PS))
