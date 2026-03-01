import sys

def suffix_array(s):
    suffix_arr = list(range(len(s)))
    rank = [ord(c) for c in s]

    i = 1
    while i < len(s):
        suffix_arr.sort(key=lambda x: (rank[x], rank[x + i] if x + i < len(s) else -1))
        
        temp = [0] * len(s)

        for j in range(1, len(s)):
            prv, cur = suffix_arr[j - 1], suffix_arr[j]
            temp[cur] = temp[prv]

            check1 = rank[prv + i] if prv + i < len(s) else -1
            check2 = rank[cur + i] if cur + i < len(s) else -1
            if rank[prv] != rank[cur] or check1 != check2:
                temp[cur] += 1

        rank = temp[:]
        i *= 2

        if rank[suffix_arr[-1]] == len(s) - 1:
            break

    return suffix_arr

S = sys.stdin.readline().rstrip()

print(*suffix_array(S), sep='\n')