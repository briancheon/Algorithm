import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        
    def update_lazy(self, start, end, index):
        if self.lazy[index] != 0:
            self.tree[index] = (end - start + 1) - self.tree[index]  
             
            if start != end:
                self.lazy[index * 2] ^= 1
                self.lazy[index * 2 + 1] ^= 1
            
            self.lazy[index] = 0

    def interval_sum(self, start, end, index, left, right):
        self.update_lazy(start, end, index)
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        
        return self.interval_sum(start, mid, index * 2, left, right) + self.interval_sum(mid + 1, end, index * 2 + 1, left, right)
        
    def update_tree(self, start, end, index, left, right):
        self.update_lazy(start, end, index)
        
        if right < start or left > end:
            return

        if left <= start and end <= right:
            self.tree[index] = (end - start + 1) - self.tree[index]
            
            if start != end:
                self.lazy[index * 2] ^= 1
                self.lazy[index * 2 + 1] ^= 1
            
            return 
        
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, left, right)
        self.update_tree(mid + 1, end, index * 2 + 1, left, right)
        
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
        

N, M = map(int, sys.stdin.readline().split())
n_ls = [0] * N

seg_tree = SegmentTree(n_ls)

for _ in range(M):
    O, S, T = map(int, sys.stdin.readline().split())
    if O == 0:
        seg_tree.update_tree(0, N - 1, 1, S - 1, T - 1)
    
    else:
        print(seg_tree.interval_sum(0, N - 1, 1, S - 1, T - 1))