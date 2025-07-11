"""
Implementation of the Fenwick Tree also know as the Binary Indexed Tree (BIT)
This is an implementation of the fenwick tree for interval sum queries.
"""
class FenwickTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)

    def build(self):
        for i in range(1, self.n + 1):
            self.update(i, self.arr[i])

    def prefix_sum(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= (idx & -idx)

        return result

    def interval_sum(self, start, end):
        return self.prefix_sum(end) - self.prefix_sum(start - 1)

    def update(self, idx, diff):
        while idx <= self.n:
            self.tree[idx] += diff
            idx += (idx & -idx)