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
        
        self.tree[index] = self.create_tree(start, mid, index * 2) + self.create_tree(mid + 1, end, index * 2 + 1)
        return self.tree[index]       
        
    def interval_sum(self, start, end, index, left, right):
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        
        return self.interval_sum(start, mid, index * 2, left, right) + self.interval_sum(mid + 1, end, index * 2 + 1, left, right)
        
    def update_tree(self, start, end, index, node, value):
        if node < start or node > end:
            return

        if start == end:
            self.tree[index] = value
            return 
        
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, node, value)
        self.update_tree(mid + 1, end, index * 2 + 1, node, value)
        
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
        

N, M = map(int, sys.stdin.readline().split())
n_ls = [0] * N

seg_tree = SegmentTree(n_ls)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        seg_tree.update_tree(0, len(n_ls) - 1, 1, b - 1, c)
    
    else:
        if b > c:
            b, c = c, b
        print(seg_tree.interval_sum(0, len(n_ls) - 1, 1, b - 1, c - 1))