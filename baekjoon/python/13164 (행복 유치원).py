import sys

N, K = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))
s_difference = []

for c in range(N - 1):
    s_difference.append((students[c + 1] - students[c], c))

s_difference.sort(reverse=True)
p_index = [0]
for c in range(K - 1):
    p_index.append(s_difference[c][1] + 1)

p_index.sort()
p_index.append(N)
total = 0

for c in range(K):
    part = students[p_index[c]:p_index[c + 1]]
    total += part[-1] - part[0]

print(total)
