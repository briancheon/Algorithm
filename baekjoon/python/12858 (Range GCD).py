import sys

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

        self.tree = [1] * (self.n * 4)
        self.lazy = [1] * (self.n * 4)

        self.build(0, self.n - 1, 1)

    def build(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]
        
        mid = (start + end) // 2

        self.tree[index] = gcd(self.build(start, mid, index * 2), self.build(mid + 1, end, index * 2 + 1))

    def query(self, start, end, index, left, right):
        ...

    def update(self, start, end, index, left, right, value):
        ...

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

seg_tree = SegmentTree(A)

Q = int(sys.stdin.readline().rstrip())
for _ in range(Q):
    T, A, B = map(int, sys.stdin.readline().split())

    if T == 0:
        print(seg_tree.query(0, N - 1, 1, A - 1, B - 1))

    else:
        seg_tree.update(0, N - 1, 1, A - 1, B - 1, T)