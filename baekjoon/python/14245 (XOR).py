import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        
        self.create_tree(0, self.n - 1, 1)
    
    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]
        
        mid = (start + end) // 2
        
        self.tree[index] = self.create_tree(start, mid, index * 2) ^ self.create_tree(mid + 1, end, index * 2 + 1)
        return self.tree[index]       
    
    def update_lazy(self, start, end, index):
        if self.lazy[index]:
            self.tree[index] ^= (end - start + 1) * self.lazy[index]
            
            if start != end:
                self.lazy[index * 2] ^= self.lazy[index]
                self.lazy[index * 2 + 1] ^= self.lazy[index]
                
            self.lazy[index] = 0
    
    def interval_sum(self, start, end, index, left, right):
        self.update_lazy(start, end, index)
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        
        return self.interval_sum(start, mid, index * 2, left, right) ^ self.interval_sum(mid + 1, end, index * 2 + 1, left, right)
        
    def update_tree(self, start, end, index, left, right, value):
        self.update_lazy(start, end, index)
        if right < start or left > end:
            return

        if left <= start and right >= end:
            self.tree[index] ^= (end - start + 1) * value
            
            if start != end:
                self.lazy[index * 2] ^= value
                self.lazy[index * 2 + 1] ^= value
            
            return 
        
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, left, right, value)
        self.update_tree(mid + 1, end, index * 2 + 1, left, right, value)
        
        self.tree[index] = self.tree[index * 2] ^ self.tree[index * 2 + 1]
        

N = int(sys.stdin.readline().rstrip())
n_ls = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())

seg_tree = SegmentTree(n_ls)

for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        a, b, c = query[1:]
        seg_tree.update_tree(0, N - 1, 1, a, b, c)
    
    else:
        a = query[1]
        print(seg_tree.interval_sum(0, N - 1, 1, a, a))