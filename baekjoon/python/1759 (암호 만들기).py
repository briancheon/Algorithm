from itertools import combinations


def comb(m, l, add):
    l, size, maximum = list(l), m - len(l), len(add)
    combs = list(map(lambda x: ''.join(sorted((*x, *l))), combinations(add, size)))
    return combs


L, C = map(int, input().split())

alphabets = list(input().split())

vowels = sorted([c for c in 'aeiou' if c in alphabets])
consonants = sorted([c for c in alphabets if c not in vowels])

results = []

for a in range(1, L - 1):
    c_vowels = list(map(lambda x: ''.join(x), combinations(vowels, a)))
    for b in range(len(c_vowels)):
        results.extend(comb(L, c_vowels[b], consonants))

results.sort()
print(*results, sep='\n')
