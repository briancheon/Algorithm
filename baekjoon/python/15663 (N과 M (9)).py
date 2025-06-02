import sys

def backtracking(n, m, ls, ans, visited, visited_idx):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(n):
        if i not in visited_idx:
            visited_idx.add(i)
            ans.append(ls[i])
            if tuple(ans) not in visited:
                visited.add(tuple(ans))
                backtracking(n, m, ls, ans, visited, visited_idx)
            ans.pop()
            visited_idx.remove(i)

N, M = map(int, sys.stdin.readline().split())
nums = sorted(map(int, sys.stdin.readline().split()))
backtracking(N, M, nums, [], set(), set())