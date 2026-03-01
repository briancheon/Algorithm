import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        
        self.create_tree(0, self.n - 1, 1)
        
    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]
        
        mid = (start + end) // 2
        self.tree[index] = min(self.create_tree(start, mid, index * 2), self.create_tree(mid + 1, end, index * 2 + 1))
        return self.tree[index]
                
    def interval_min(self, start, end, index, left, right):
        if left > end or right < start:
            return float('inf')
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        return min(self.interval_min(start, mid, index * 2, left, right), self.interval_min(mid + 1, end, index * 2 + 1, left, right))
       

N, M = map(int, sys.stdin.readline().split())
n_ls = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

seg_tree = SegmentTree(n_ls)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(seg_tree.interval_min(0, N -  1, 1, a - 1, b - 1))
    
