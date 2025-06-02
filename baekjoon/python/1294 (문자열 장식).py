import sys
from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return 1
    elif x + y == y + x:
        return 0
    else:
        return -1

N = int(sys.stdin.readline().rstrip())

words = [sys.stdin.readline().rstrip() for _ in range(N)]

W = ""

while words:
    words.sort(key=cmp_to_key(compare))
    if len(words[0]) == 1:
        print(words.pop(0), end='')
    else:
        print(words[0][0], end='')
        words[0] = words[0][1:]
