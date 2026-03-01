target, n = map(int, input().split())

for c in range(n, 101):
    a = ((2 * target / c) - c + 1) / 2
    if a < 0:
        break
    if a == int(a):
        a = int(a)
        print(*[i for i in range(a, a + c)])
        exit()
print(-1)
