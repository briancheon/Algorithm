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
    
    def insert(self, start, end, index, value):
        if start == end:
            self.tree[index] += 1
            return self.tree[index]
        
        mid = (start + end) // 2
        
        if value <= mid:
            self.insert(start, mid, index * 2, value)
            
        else:
            self.insert(mid + 1, end, index * 2 + 1, value)
        
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
        
        return self.tree[index]
        
    def pop(self, start, end, index, pos):
        self.tree[index] -= 1
        
        if start == end:
            return start
        
        mid = (start + end) // 2
        
        if pos <= self.tree[index * 2]:
            return self.pop(start, mid, index * 2, pos)
            
        else:
            return self.pop(mid + 1, end, index * 2 + 1, pos - self.tree[index * 2])
        
        
N = int(sys.stdin.readline().rstrip())
A = [0] * (1 << 20)

seg_tree = SegmentTree(A)

for _ in range(N):
    S, X = map(int, sys.stdin.readline().split())
    if S == 1:
        seg_tree.insert(0, 2000000, 1, X)
        
    else:
        print(seg_tree.pop(0, 2000000, 1, X))