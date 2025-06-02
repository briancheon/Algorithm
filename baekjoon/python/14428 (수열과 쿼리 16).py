import sys


def minimum(a, b):
    if a[1] > b[1]:
        return b
    return a


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
        
        self.tree[index] = minimum(self.create_tree(start, mid, index * 2), self.create_tree(mid + 1, end, index * 2 + 1))
        return self.tree[index]
        
    def interval_min(self, start, end, index, left, right):
        if left > end or right < start:
            return (float('inf'), float('inf'))
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        
        return minimum(self.interval_min(start, mid, index * 2, left, right), self.interval_min(mid + 1, end, index * 2 + 1, left, right))
                
    def update_tree(self, start, end, index, node, value):
        if node < start or node > end:
            return
        
        if start == end:
            self.tree[index] = (node + 1, value)
            return
        
        mid = (start + end) // 2
    
        self.update_tree(start, mid, index * 2, node, value)
        self.update_tree(mid + 1, end, index * 2 + 1, node, value)
        
        self.tree[index] = minimum(self.tree[index * 2], self.tree[index * 2 + 1])
        
        
N = int(sys.stdin.readline().rstrip())
A = list(enumerate(map(int, sys.stdin.readline().split()), 1))

seg_tree = SegmentTree(A)

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        seg_tree.update_tree(0, N - 1, 1, b - 1, c)
        
    else:
        print(seg_tree.interval_min(0, N - 1, 1, b - 1, c - 1)[0])