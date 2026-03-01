import sys

def build_prefix(pattern):
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            prefix[i] = j
    return prefix

def kmp(text, pattern):
    prefix = build_prefix(pattern)
    match = []
    j = 0
    for i in range(len(text)):
        while j and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                match.append(i - len(pattern) + 1)
                j = prefix[j - 1]
    return match

def dist(n, a, b):
    return min(abs(a - b), n - abs(a - b))

def dist_sum(n, a, b, c):
    return min(dist(n, a, b) + dist(n, a, c), dist(n, b, a) + dist(n, b, c), dist(n, c, a) + dist(n, c, b))    

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()

best = float("inf")

for rotation in range(len(s1)):
    transform = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            transform.append('#')
        else:
            transform.append(chr(3 * ord('B') - ord(s1[i]) - ord(s2[i])))

    transform = ''.join(transform)

    for match_idx in kmp(s3 + s3, transform):
        best = min(best, dist_sum(len(s1), 0, rotation, match_idx))

    s2 = s2[1:] + s2[0]

print(-1 if best == float("inf") else best)