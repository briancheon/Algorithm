import sys

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def minimum_distance(n, _point):
    if n == 1:
        return 1, 4

    _x = sorted([_point[_][0] for _ in range(n)])
    _y = sorted([_point[_][1] for _ in range(n)])

    dist = 0
    for i in range(n):
        dist += manhattan_distance((_x[n // 2], _y[n // 2]), _point[i])

    if n % 2:
        if (_x[n // 2], _y[n // 2]) not in _point:
            return dist, 1
        else:
            count = 0
            check = [
                (_x[n // 2] - 1, _y[n // 2]),
                (_x[n // 2] + 1, _y[n // 2]),
                (_x[n // 2], _y[n // 2] - 1),
                (_x[n // 2], _y[n // 2] + 1)
            ]
            for i in check:
                if _x[0] <= i[0] < _x[-1] and _y[0] <= i[1] <= _y[-1]:
                    count += 1
            if count != 0:
                return dist + 1, count

    else:
        count = (_x[n // 2] - _x[n // 2 - 1] + 1) * (_y[n // 2] - _y[n // 2 - 1] + 1)
        for i in range(n):
            p = _point[i]
            if (p[0] == _x[n // 2] or p[0] == _x[n // 2 - 1]) and _y[n // 2 - 1] <= p[1] <= _y[n // 2]:
                count -= 1
            elif (p[1] == _y[n // 2] or p[1] == _y[n // 2 - 1]) and _x[n // 2 - 1] <= p[0] <= _x[n // 2]:
                count -= 1
        if count != 0:
            return dist, count

    if count == 0:
        _point = list(sorted(_point))
        _d, visited = [], []
        for i in range(n):
            x, y = _point[i]
            _check = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y + 1)]
            for check in _check:
                if check not in _point and check not in visited:
                    visited.append(check)
                    dist = 0
                    for j in range(n):
                        dist += manhattan_distance(check, _point[j])
                    _d.append(dist)
        return min(_d), _d.count(min(_d))

T = int(sys.stdin.readline().rstrip())

for c in range(T):
    N = int(sys.stdin.readline().rstrip())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    min_dist, p_count = minimum_distance(N, points)

    print(min_dist, p_count)
