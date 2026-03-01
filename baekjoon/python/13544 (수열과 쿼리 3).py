import sys
import bisect

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [[] for _ in range(4 * self.n)]
        self.create_tree(0, self.n - 1, 1)

    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = [self.arr[start]]
        else:
            mid = (start + end) // 2
            self.create_tree(start, mid, index * 2)
            self.create_tree(mid + 1, end, index * 2 + 1)
            self.tree[index] = sorted(self.tree[index * 2] + self.tree[index * 2 + 1])

    def interval_count(self, start, end, index, left, right, value):
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return len(self.tree[index]) - bisect.bisect_right(self.tree[index], value)
        
        mid = (start + end) // 2
        return self.interval_count(start, mid, index * 2, left, right, value) + self.interval_count(mid + 1, end, index * 2 + 1, left, right, value)


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

seg_tree = SegmentTree(A)

M = int(sys.stdin.readline().rstrip())
last_ans = 0
for _ in range(M):
    a, b, c = map(lambda x: int(x) ^ last_ans, sys.stdin.readline().split())
    last_ans = seg_tree.interval_count(0, N - 1, 1, a - 1, b - 1, c)
    print(last_ans)