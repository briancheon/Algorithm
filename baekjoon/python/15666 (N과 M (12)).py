import sys

def backtracking(n, m, ls, ans, visited):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in ls:
        if not ans or i >= ans[-1]:
            ans.append(i)
            if tuple(ans) not in visited:
                visited.add(tuple(ans))
                backtracking(n, m, ls, ans, visited)
            ans.pop()


N, M = map(int, sys.stdin.readline().split())
nums = sorted(map(int, sys.stdin.readline().split()))
backtracking(N, M, nums, [], set())