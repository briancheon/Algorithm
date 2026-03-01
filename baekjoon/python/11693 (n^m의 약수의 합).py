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


def remainder(base, exp, m):  # Calculate base ** exp mod m
    init = 2
    powers = [base]
    # Calculate base powers until exp
    while init <= exp:
        powers.append((powers[-1] ** 2) % m)
        init *= 2
    binary = bin(exp)[2:][::-1]
    product = 1
    # We can now multiply the correct powers
    for i in range(len(binary)):
        if binary[i] == '1':
            product *= powers[i]
            product %= m
    return product


N, M = map(int, input().split())

factors, powers = p_fact(N)
print(factors, powers)
result = 1

for c in range(len(factors)):
    r = remainder(factors[c], powers[c] * M, 1000000007)
    # ((bases[c] ** (powers[c] + 1) - 1) // (bases[c] - 1))
    result *= r

print(result % 1000000007)

