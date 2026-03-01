import sys

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
        
        self.tree[index] = self.create_tree(start, mid, index * 2) + self.create_tree(mid + 1, end, index * 2 + 1)
        return self.tree[index]       
        
    def interval_sum(self, start, end, index, left, right):
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return self.tree[index]
        
        mid = (start + end) // 2
        
        return self.interval_sum(start, mid, index * 2, left, right) + self.interval_sum(mid + 1, end, index * 2 + 1, left, right)
        
    def update_tree(self, start, end, index, node, value):
        if node < start or node > end:
            return

        if start == end:
            self.tree[index] = value
            return 
        
        mid = (start + end) // 2
        self.update_tree(start, mid, index * 2, node, value)
        self.update_tree(mid + 1, end, index * 2 + 1, node, value)
        
        self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]
        

N = int(sys.stdin.readline().rstrip())
n_ls = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
query1, query2 = [], []

seg_tree = SegmentTree(n_ls)
q_num = 0

for i in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        query1.append(query[1:])
    
    else:
        query2.append([q_num] + query[1:])
        q_num += 1
        
query2.sort(key=lambda x: x[1])
state = 0

result = {}

for q in query2:
    idx, k, i, j = q
    if k == 0:
        result[idx] = seg_tree.interval_sum(0, N - 1, 1, i - 1, j - 1)
        continue
        
    if state < k:
        for c in range(state, k):
            seg_tree.update_tree(0, N - 1, 1, query1[c][0] - 1, query1[c][1])
            
        state = k
        
    result[idx] = seg_tree.interval_sum(0, N - 1, 1, i - 1, j - 1)

for i in range(len(query2)):
    print(result[i])