import sys

def bin_search(arr):
    start, end = 0, N - 1
    best = (float('inf'), arr[0], arr[-1])

    while start < end:
        cur_sum = arr[start] + arr[end]
        if abs(cur_sum) < best[0]:
            best = (abs(cur_sum), arr[start], arr[end])
        
        if cur_sum == 0:
            return best
        
        if cur_sum < 0:
            start += 1

        else:
            end -= 1

    return best

N = int(sys.stdin.readline().rstrip())
solutions = list(map(int, sys.stdin.readline().split()))

_, sol1, sol2 = bin_search(solutions)
print(sol1, sol2)
