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

words = list(sorted([sys.stdin.readline().rstrip() for _ in range(N)], key=cmp_to_key(compare)))
print(words)
W = ""

while len(words) > 1:
    i = j = 0
    w1, w2, result = words[0], words[1], ""
    print(w1, w2)
    while i < len(w1) and j < len(w2):
        if w1[i] <= w2[j]:
            result += w1[i]
            i += 1
        else:
            result += w2[j]
            j += 1

    while i < len(w1):
        result += w1[i]
        i += 1

    while j < len(w2):
        result += w2[j]
        j += 1

    words[0:2] = [result]
    print(words, result)

print(words[0])
