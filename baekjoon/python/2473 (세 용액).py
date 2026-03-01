
import sys

def bin_search(arr):
    n = len(arr)
    best_sum = float('inf')
    solution = (0, 0, 0)

    for i in range(n - 2):
        start, end = i + 1, n - 1
        while start < end:
            current_sum = arr[i] + arr[start] + arr[end]
            if abs(current_sum) < best_sum:
                best_sum = abs(current_sum)
                solution = (arr[i], arr[start], arr[end])

                if best_sum == 0:
                    return solution

            if current_sum < 0:
                start += 1

            else:
                end -= 1

    return solution

N = int(sys.stdin.readline().rstrip())
solutions = sorted(map(int, sys.stdin.readline().split()))
print(*bin_search(solutions))