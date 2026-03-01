import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    OX = sys.stdin.readline().rstrip()
    _OX = []
    temp = ""
    for s in OX:
        if s == "X":
            _OX.append(temp)
            temp = ""
        else:
            temp += s
    _OX.append(temp)
    print(sum(map(lambda x: len(x) * (len(x) + 1) // 2, _OX)))
