import sys

def backtracking(n, m, ls, ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in ls:
        if i not in ans:
            ans.append(i)
            backtracking(n, m, ls, ans)
            ans.pop()

N, M = map(int, sys.stdin.readline().split())
nums = sorted(map(int, sys.stdin.readline().split()))
backtracking(N, M, nums, [])