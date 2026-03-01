import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        
        self.create_tree(0, self.n - 1, 1)
        
    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = (self.arr[start], self.arr[start])
            return self.tree[index]
        
        mid = (start + end) // 2
        left_child = self.create_tree(start, mid, index * 2)
        right_child = self.create_tree(mid + 1, end, index * 2 + 1)
        
        self.tree[index] = (min(left_child[0], right_child[0]), max(left_child[1], right_child[1]))
        return self.tree[index]
                
    def interval_minmax(self, start, end, index, left, right):
        if left > end or right < start:
            return (float('inf'), float('-inf'))
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        left_child = self.interval_minmax(start, mid, index * 2, left, right)
        right_child = self.interval_minmax(mid + 1, end, index * 2 + 1, left, right)
        return (min(left_child[0], right_child[0]), max(left_child[1], right_child[1]))
        

N, M = map(int, sys.stdin.readline().split())
n_ls = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

seg_tree = SegmentTree(n_ls)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(*seg_tree.interval_minmax(0, N - 1, 1, a - 1, b - 1))