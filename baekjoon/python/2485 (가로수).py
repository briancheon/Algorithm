import sys
from math import gcd
from functools import reduce

N = int(sys.stdin.readline().rstrip())

gap = []
trees = []

for c in range(N):
    tree = int(sys.stdin.readline().rstrip())
    trees.append(tree)

for c in range(N - 1):
    gap.append(trees[c + 1] - trees[c])

min_gap = reduce(lambda x, y: gcd(x, y), gap)
print((trees[-1] - trees[0]) // min_gap - len(trees) + 1)
