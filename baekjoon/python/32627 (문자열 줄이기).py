import sys

N, M = map(int, sys.stdin.readline().split())
string = sys.stdin.readline().rstrip()

cnt, skip_cnt = [0] * 26, [0] * 26
answer = ""

for s in string:
    cnt[ord(s) - 97] += 1
    
for i in range(26):
    if cnt[i] > M:
        skip_cnt[i] = M
        break
    skip_cnt[i] = cnt[i]
    M -= cnt[i]

for s in string:
    if skip_cnt[ord(s) - 97] > 0:
        skip_cnt[ord(s) - 97] -= 1
        continue
    answer += s
    
print(answer)