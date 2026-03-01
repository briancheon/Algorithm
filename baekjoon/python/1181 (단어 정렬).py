import sys

N = int(sys.stdin.readline().rstrip())

words = set()
for c in range(N):
    words.add(sys.stdin.readline().rstrip())

words = list(words)
words.sort(key=lambda x: (len(x), x))
print(*words, sep='\n')
