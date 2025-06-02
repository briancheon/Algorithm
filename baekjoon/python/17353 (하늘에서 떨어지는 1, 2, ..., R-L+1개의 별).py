import sys

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)

        self.lazyA = [0] * (4 * self.n)
        self.lazyB = [0] * (4 * self.n)
        
        self.create_tree(0, self.n - 1, 1)
    
    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]
        mid = (start + end) // 2
        self.tree[index] = self.create_tree(start, mid, index * 2) + self.create_tree(mid + 1, end, index * 2 + 1)
        return self.tree[index]
    
    def _apply(self, index, start, end, a, b):
        count = end - start + 1
        total_index_sum = (start + end) * count // 2
        self.tree[index] += a * total_index_sum + b * count

        self.lazyA[index] += a
        self.lazyB[index] += b

    def push_down(self, start, end, index):
        if self.lazyA[index] == 0 and self.lazyB[index] == 0:
            return
        mid = (start + end) // 2

        self._apply(index * 2, start, mid, self.lazyA[index], self.lazyB[index])
        self._apply(index * 2 + 1, mid + 1, end, self.lazyA[index], self.lazyB[index])

        self.lazyA[index] = 0
        self.lazyB[index] = 0
    
    def update_tree(self, start, end, index, l, r, a, b):
        if r < start or l > end:
            return
        
        if l <= start and end <= r:
            self._apply(index, start, end, a, b)
            return

        self.push_down(start, end, index)
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, l, r, a, b)
        self.update_tree(mid + 1, end, index * 2 + 1, l, r, a, b)

        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
    
    def interval_sum(self, start, end, index, l, r):
        if r < start or l > end:
            return 0
        if l <= start and end <= r:
            return self.tree[index]
        self.push_down(start, end, index)
        mid = (start + end) // 2
        return self.interval_sum(start, mid, index * 2, l, r) + self.interval_sum(mid + 1, end, index * 2 + 1, l, r)

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

Q = int(sys.stdin.readline().rstrip())

seg_tree = SegmentTree(A)

for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        L, R = query[1:]
        seg_tree.update_tree(0, N - 1, 1, L - 1, R - 1, 1, 2 - L)
    else:
        X = query[1]
        print(seg_tree.interval_sum(0, N - 1, 1, X - 1, X - 1))