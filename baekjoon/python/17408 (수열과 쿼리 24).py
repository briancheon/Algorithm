import sys

class Node:
    def __init__(self, max1, max2):
        self.max1 = max1
        self.max2 = max2

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(self.arr)

        self.tree = [Node(0, 0)] * (4 * self.n)
        self.build(0, self.n - 1, 1)

    def build(self, start, end, index):
        if start == end:
            self.tree[index] = Node(self.arr[start], 0)
            return self.tree[index]
        
        mid = (start + end) // 2
        left_child = self.build(start, mid, index * 2)
        right_child = self.build(mid + 1, end, index * 2 + 1)
        
        self.tree[index] = Node(max(left_child.max1, right_child.max1), max(left_child.max2, right_child.max2, min(left_child.max1, right_child.max1)))
        return self.tree[index]

    def query(self, start, end, index, left, right):
        if left > end or right < start:
            return Node(0, 0)
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        left_child = self.query(start, mid, index * 2, left, right)
        right_child = self.query(mid + 1, end, index * 2 + 1, left, right)

        return Node(max(left_child.max1, right_child.max1), max(left_child.max2, right_child.max2, min(left_child.max1, right_child.max1)))

    def update(self, start, end, index, node, val):
        if node < start or node > end:
            return
        
        if start == end:
            self.tree[index] = Node(val, 0)
            return

        mid = (start + end) // 2
        self.update(start, mid, index * 2, node, val)
        self.update(mid + 1, end, index * 2 + 1, node, val)

        left_child = self.tree[index * 2]
        right_child = self.tree[index * 2 + 1]

        self.tree[index] = Node(max(left_child.max1, right_child.max1), max(left_child.max2, right_child.max2, min(left_child.max1, right_child.max1)))

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

seg_tree = SegmentTree(A)

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
       i, v = query[1:]
       seg_tree.update(0, N - 1, 1, i - 1, v)

    else:
        l, r = query[1:]
        q = seg_tree.query(0, N - 1, 1, l - 1, r - 1)
        print(q.max1 + q.max2)