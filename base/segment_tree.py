"""
Implementation of a segment tree for sum query
* Lazy propagation not implemented (for later) *
"""
class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

        # Initialize the tree with 4 * n elements
        self.tree = [0] * (4 * self.n)

        # Build the segment tree
        self.build(0, self.n - 1, 1)

    def build(self, start, end, index):
        # Leaf node, store the value of the array
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]

        mid = (start + end) // 2
        # Recursively build the left and right subtrees
        self.tree[index] = self.build(start, mid, index * 2) + self.build(mid + 1, end, index * 2 + 1)

        return self.tree[index]

    def query(self, start, end, index, left, right):
        # If the range is completely outside the query range
        if left > end or right < start:
            return 0

        # If the range is completely inside the query range
        if left <= start and right >= end:
            return self.tree[index]

        mid = (start + end) // 2
        # Recursively query the left and right subtrees
        return self.query(start, mid, index * 2, left, right) + self.query(mid + 1, end, index * 2 + 1, left, right)

    def update(self, start, end, index, node, val):
        # Return if node is outside the range
        if node < start or node > end:
            return

        # Update leaf node if we have reached it
        if start == end:
            self.tree[index] = val
            return

        mid = (start + end) // 2
        # Recursively update the left and right subtrees
        self.update(start, mid, index * 2, node, val)
        self.update(mid + 1, end, index * 2 + 1, node, val)

        # Recalculate the value of the current node
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
