import sys

class Node:
    def __init__(self, max1, max2, max_cnt, s):
        self.max1 = max1
        self.max2 = max2
        self.max_cnt = max_cnt
        self.s = s

def compare_nodes(a, b):
    if a.max1 == b.max1:
        return Node(a.max1, max(a.max2, b.max2), a.max_cnt + b.max_cnt, a.s + b.s)
    
    if a.max1 > b.max1:
        a, b = b, a

    return Node(b.max1, max(a.max1, b.max2), b.max_cnt, a.s + b.s)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [None] * (self.n * 4)
        self.lazy = [None] * (self.n * 4)
        self.build(0, self.n - 1, 1)

    def build(self, start, end, index):
        if start == end:
            self.tree[index] = Node(self.arr[start], -1, 1, self.arr[start])
            return
        
        mid = (start + end) >> 1
        self.build(start, mid, index << 1)
        self.build(mid + 1, end, (index << 1) | 1)
        self.tree[index] = compare_nodes(self.tree[index << 1], self.tree[(index << 1) | 1])

    def push(self, start, end, index):
        v = self.lazy[index]
        if v is None:
            return
        node = self.tree[index]
        if node.max1 <= v:
            self.lazy[index] = None
            return
        node.s -= node.max_cnt * (node.max1 - v)
        node.max1 = v
        if start != end:
            for child in (index << 1, (index << 1) | 1):
                if self.lazy[child] is None or self.lazy[child] > v:
                    self.lazy[child] = v if self.lazy[child] is None else min(self.lazy[child], v)
        self.lazy[index] = None

    def update(self, start, end, index, left, right, value):
        self.push(start, end, index)
        node = self.tree[index]
        if right < start or end < left or node.max1 <= value:
            return
        
        if left <= start and end <= right and node.max2 < value:
            self.lazy[index] = value
            self.push(start, end, index)
            return
        
        mid = (start + end) >> 1
        self.update(start, mid, index << 1, left, right, value)
        self.update(mid + 1, end, (index << 1) | 1, left, right, value)
        self.tree[index] = compare_nodes(self.tree[index << 1], self.tree[(index << 1) | 1])

    def query_max(self, start, end, index, left, right):
        self.push(start, end, index)
        if right < start or end < left:
            return float('-inf')
        
        if left <= start and end <= right:
            return self.tree[index].max1
        
        mid = (start + end) >> 1
        return max(self.query_max(start, mid, index << 1, left, right), self.query_max(mid + 1, end, (index << 1) | 1, left, right))

    def query_sum(self, start, end, index, left, right):
        self.push(start, end, index)
        if right < start or end < left:
            return 0
        
        if left <= start and end <= right:
            return self.tree[index].s
        
        mid = (start + end) >> 1
        return self.query_sum(start, mid, index << 1, left, right) + self.query_sum(start, end, (index << 1) | 1, left, right)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

seg_tree = SegmentTree(A)

M = int(sys.stdin.readline())
for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        L, R, X = query[1:]
        seg_tree.update(0, N - 1, 1, L - 1, R - 1, X)

    elif query[0] == 2:
        L, R = query[1:]
        print(seg_tree.query_max(0, N - 1, 1, L - 1, R - 1))

    else:
        L, R = query[1:]
        print(seg_tree.query_sum(0, N - 1, 1, L - 1, R - 1))