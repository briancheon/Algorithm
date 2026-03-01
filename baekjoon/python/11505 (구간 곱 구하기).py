import sys

MOD = 1000000007

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
        
        self.tree[index] = self.create_tree(start, mid, index * 2) * self.create_tree(mid + 1, end, index * 2 + 1) % MOD
        return self.tree[index]
    
    def interval_product(self, start, end, index, left, right):
        if left > end or right < start:
            return 1
        
        if left <= start and right >= end:
            return self.tree[index] % MOD
        
        mid = (start + end) // 2
        
        return self.interval_product(start, mid, index * 2, left, right) * self.interval_product(mid + 1, end, index * 2 + 1, left, right) % MOD
            
    def update_tree(self, start, end, index, node, value):
        if node < start or node > end:
            return
        
        if start == end:
            self.tree[index] = value
            return
        
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, node, value)
        self.update_tree(mid + 1, end, index * 2 + 1, node, value)
        
        self.tree[index] = self.tree[index * 2] * self.tree[index * 2 + 1] % MOD
        
N, M, K = map(int, sys.stdin.readline().split())
n_ls = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

seg_tree = SegmentTree(n_ls)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        seg_tree.update_tree(0, len(n_ls) - 1, 1, b - 1, c)
    
    else:
        print(seg_tree.interval_product(0, len(n_ls) - 1, 1, b - 1, c - 1))