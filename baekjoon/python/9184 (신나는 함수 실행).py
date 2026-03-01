def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a <= b <= c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


_n = []
n = list(map(int, input().split()))

while n != [-1, -1, -1]:
    string = "w(%d, %d, %d) = %d" % (*n, w(*n))
    print(string)
    _n.append(string)
    n = list(map(int, input().split()))

print(*_n, sep='\n')
