import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
words = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        words[word] += 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(words)):
    print(words[i][0])
