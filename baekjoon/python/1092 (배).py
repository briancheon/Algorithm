import sys
import math

N = int(sys.stdin.readline().rstrip())
crane = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
_box = list(map(int, sys.stdin.readline().split()))

time = 0
crane.sort(reverse=True)
_box.sort(reverse=True)

if max(crane) < max(_box):
    print(-1)

else:
    while sum(_box) > 0:
        if all(i < min(crane) for i in _box):
            time += math.ceil(len([ele for ele in _box if ele != 0]) / len(crane))
            break
        else:
            i = 0
            for box in range(len(_box)):
                if _box[box - i] <= crane[i]:
                    _box.pop(box - i)
                    i += 1
                    if i == N:
                        break
        time += 1

    print(time)
