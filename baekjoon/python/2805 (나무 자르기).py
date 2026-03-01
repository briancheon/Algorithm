import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
max_tree = max(trees)

low, high = 0, max_tree

while low <= high:
    mid = (low + high) // 2

    total_tree_cut = sum(tree - mid for tree in trees if tree > mid)
            
    if total_tree_cut < M:
        high = mid - 1
    else:
        low = mid + 1
        
print(high)