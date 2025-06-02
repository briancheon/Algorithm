import sys

MOD = 1000000007

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.lazy = [[1, 0] for _ in range(4 * self.n)]
        
        self.create_tree(0, self.n - 1, 1)
    
    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]
        
        mid = (start + end) // 2
        
        self.tree[index] = self.create_tree(start, mid, index * 2) + self.create_tree(mid + 1, end, index * 2 + 1)
        return self.tree[index]
        
    def update_lazy(self, start, end, index):
        if start != end:
            for i in range(2):
                self.lazy[index * 2][i] = (self.lazy[index * 2][i] * self.lazy[index][0]) % MOD
                self.lazy[index * 2 + 1][i] = (self.lazy[index * 2 + 1][i] * self.lazy[index][0]) % MOD
            
            self.lazy[index * 2][1] = (self.lazy[index * 2][1] + self.lazy[index][1]) % MOD
            self.lazy[index * 2 + 1][1] = (self.lazy[index * 2 + 1][1] + self.lazy[index][1]) % MOD
            
        self.tree[index] = (self.tree[index] * self.lazy[index][0]) % MOD
        self.tree[index] = (self.tree[index] + (end - start + 1) * self.lazy[index][1]) % MOD
        
        self.lazy[index][0] = 1
        self.lazy[index][1] = 0

    def interval_sum(self, start, end, index, left, right):
        self.update_lazy(start, end, index)
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return self.tree[index] % MOD
        
        mid = (start + end) // 2
        
        return (self.interval_sum(start, mid, index * 2, left, right) + self.interval_sum(mid + 1, end, index * 2 + 1, left, right)) % MOD
        
    def update_tree(self, start, end, index, operation, left, right, value):
        self.update_lazy(start, end, index)
        
        if right < start or left > end:
            return

        if left <= start and end <= right:
            if operation == 1:
                self.lazy[index][1] = (self.lazy[index][1] + value) % MOD
                
            elif operation == 2:
                self.lazy[index][0] = (self.lazy[index][0] * value) % MOD
                self.lazy[index][1] = (self.lazy[index][1] * value) % MOD
                
            else:
                self.lazy[index][0] = 0
                self.lazy[index][1] = value
            
            self.update_lazy(start, end, index)
            return 
        
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, operation, left, right, value)
        self.update_tree(mid + 1, end, index * 2 + 1, operation, left, right, value)
        
        self.tree[index] = (self.tree[index * 2] + self.tree[index * 2 + 1]) % MOD
    

N = int(sys.stdin.readline().rstrip())
n_ls = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())

seg_tree = SegmentTree(n_ls)

for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] <= 3:
        x, y, v = query[1:]
        seg_tree.update_tree(0, N - 1, 1, query[0], x - 1, y - 1, v)
        
    else:
        x, y = query[1:]
        print(seg_tree.interval_sum(0, N - 1, 1, x - 1, y - 1) % MOD)