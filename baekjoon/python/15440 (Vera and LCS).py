import sys

N, K = map(int, sys.stdin.readline().split())
A = sys.stdin.readline().rstrip()

alphabets = "abcdefghijklmnopqrstuvwxyz"
alpha_cnt = dict.fromkeys(alphabets, 0)

for s in A:
    alpha_cnt[s] += 1

min_alpha, min_cnt = min(alpha_cnt.items(), key=lambda x: x[1])

if not (min_cnt <= K <= N):
    print("WRONGANSWER")

else:
    K -= min_cnt
    answer = [min_alpha] * N

    i = 0
    while K:
        if A[i] != answer[i]:
            answer[i] = A[i]
            K -= 1

        i += 1

    print(''.join(answer))