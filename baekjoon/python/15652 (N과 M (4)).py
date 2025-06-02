import sys

def backtracking(n, m, ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        if not ans or i >= ans[-1]:
            ans.append(i)
            backtracking(n, m, ans)
            ans.pop()

N, M = map(int, sys.stdin.readline().split())
backtracking(N, M, [])