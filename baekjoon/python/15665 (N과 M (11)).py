import sys

visited = set()
def backtracking(arr, m, ans):
    if tuple(ans) in visited:
        return

    if len(ans) == m:
        visited.add(tuple(ans))
        print(*ans)
        return
    
    for i in range(len(arr)):
        ans.append(arr[i])
        backtracking(arr, m, ans)
        ans.pop()

N, M = map(int, sys.stdin.readline().split())
ls = sorted(map(int, sys.stdin.readline().split()))
backtracking(ls, M, [])