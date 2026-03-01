import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

alphabets = defaultdict(int)
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(N):
    string = sys.stdin.readline().rstrip()
    for j in range(len(string)):
        alphabets[string[j]] += 10 ** (len(string) - j - 1)

ordered = list(sorted(alphabets.items(), key=lambda x: x[1], reverse=True))
answer = 0

for a in range(len(ordered)):
    answer += alphabets[ordered[a][0]] * nums[a]

print(answer)
