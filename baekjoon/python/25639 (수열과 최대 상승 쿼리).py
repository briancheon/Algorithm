import sys


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [(float('inf'), float('-inf'), 0)] * (4 * self.n)

        self.create_tree(0, self.n - 1, 1)

    def create_tree(self, start, end, index):
        if start == end:
            self.tree[index] = (self.arr[start], self.arr[start], 0)
            return self.tree[index]
        
        mid = (start + end) // 2
        l_node = self.create_tree(start, mid, index * 2)
        r_node = self.create_tree(mid + 1, end, index * 2 + 1)

        self.tree[index] = (min(l_node[0], r_node[0]), max(l_node[1], r_node[1]), max(r_node[1] - l_node[0], max(l_node[2], r_node[2])))

        return self.tree[index]

    def interval_max_increase(self, start, end, index, left, right):
        if left > end or right < start:
            return (float('inf'), float('-inf'), 0)
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2

        l_node = self.interval_max_increase(start, mid, index * 2, left, right)
        r_node = self.interval_max_increase(mid + 1, end, index * 2 + 1, left, right)

        return (min(l_node[0], r_node[0]), max(l_node[1], r_node[1]), max(r_node[1] - l_node[0], max(l_node[2], r_node[2])))

    def update_tree(self, start, end, index, new_idx, value):
        if new_idx > end or new_idx < start:
            return self.tree[index]
        
        if start == end:
            self.tree[index] = (value, value, 0)
            return self.tree[index]
        
        mid = (start + end) // 2

        l_node = self.update_tree(start, mid, index * 2, new_idx, value)
        r_node = self.update_tree(mid + 1, end, index * 2 + 1, new_idx, value)

        self.tree[index] = (min(l_node[0], r_node[0]), max(l_node[1], r_node[1]), max(r_node[1] - l_node[0], max(l_node[2], r_node[2])))
        return self.tree[index]
    

N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

segment_tree = SegmentTree(a)

Q = int(sys.stdin.readline().rstrip())
for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        k, x = query[1:]
        segment_tree.update_tree(0, N - 1, 1, k - 1, x)

    else:
        l, r = query[1:]
        print(segment_tree.interval_max_increase(0, N - 1, 1, l - 1, r - 1)[2])