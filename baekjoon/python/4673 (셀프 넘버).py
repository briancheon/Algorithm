def d(n):
    r = n
    while n:
        r, n = r + n % 10, n // 10
    return r

non_self = [0 for _ in range(10001)]
for i in range(1, 10001):
    check = d(i)
    if check < 10001:
        non_self[check] = 1

for i in range(1, 10001):
    if non_self[i] != 1:
        print(i)
