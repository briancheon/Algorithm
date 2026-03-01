import sys

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [float('-inf')] * (4 * self.n)
        self.build(0, self.n - 1, 1)

    def build(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return
        
        mid = (start + end) // 2
        self.build(start, mid, index * 2)
        self.build(mid + 1, end, index * 2 + 1)

        self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])

    def query_max(self, start, end, index, left, right):
        if right < start or end < left:
            return float('-inf')
        
        if left <= start and end <= right:
            return self.tree[index]
        
        mid = (start + end) // 2
        return max(self.query_max(start, mid, index * 2, left, right), self.query_max(mid + 1, end, index * 2 + 1, left, right))

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    seg_tree = SegmentTree(a)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    for i in range(n):
        max_val = seg_tree.query_max(0, n - 1, 1, 0, n - i - 1)

        print(prefix_sum[-1] - prefix_sum[-1 - i - 1] - a[-1 - i] + max_val, end=' ')

    print()