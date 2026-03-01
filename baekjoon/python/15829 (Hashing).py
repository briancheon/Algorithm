import sys

alphabets = {}
a = "abcdefghijklmnopqrstuvwxyz"
n = list(range(1, 27))
for i in range(26):
    alphabets[a[i]] = n[i]

L = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()

H = 0
for s in range(L):
    H += alphabets[string[s]] * pow(31, s, 1234567891)

print(H % 1234567891)
