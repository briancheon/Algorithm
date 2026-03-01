import sys
from functools import cmp_to_key

def compare(x, y):
    if x + y < y + x:
        return 1
    elif x + y == y + x:
        return 0
    else:
        return -1

N = int(sys.stdin.readline().rstrip())
ls = list(sys.stdin.readline().split())

if all(i == "0" for i in ls):
    print(0)

else:
    ls.sort(key=cmp_to_key(compare))
    print(''.join(ls))
