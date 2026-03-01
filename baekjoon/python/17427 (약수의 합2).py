def p_fact(n):
    i = 2
    _b = []
    _p = []
    while i < n:
        if n % i == 0:
            _b.append(i)
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            _p.append(count)
        i += 1
    if n != 1:
        _b.append(n)
        _p.append(1)
    return _b, _p


N = int(input())
bases, powers = p_fact(N)
print(bases, powers)
answer = 1

for c in range(len(bases)):
    answer *= ((bases[c] ** (powers[c] + 1) - 1) // (bases[c] - 1))

print(answer)
