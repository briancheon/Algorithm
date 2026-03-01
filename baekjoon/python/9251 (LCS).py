import sys

S1 = sys.stdin.readline().rstrip()
S2 = sys.stdin.readline().rstrip()

lcs = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            lcs[i + 1][j + 1] = lcs[i][j] + 1
        else:
            lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])

print(max(map(max, lcs)))
