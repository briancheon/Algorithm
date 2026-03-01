import sys

def max_perimeter(_l):
    _l = list(sorted(_l))

    if _l[2] >= _l[0] + _l[1]:
        _l[2] = _l[0] + _l[1] - 1

    return sum(_l)

lengths = list(map(int, sys.stdin.readline().split()))
print(max_perimeter(lengths))
