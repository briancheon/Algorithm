import sys

def backtracking(arr, m, ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in arr:
        ans.append(i)
        backtracking(arr, m, ans)
        ans.pop()

N, M = map(int, sys.stdin.readline().split())
ls = sorted(map(int, sys.stdin.readline().split()))
backtracking(ls, M, [])