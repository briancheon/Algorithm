import sys

N, M = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

class DSU:
    def __init__(self, n, genders):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = [(1, 0) if genders[i] % 2 else (0, 1) for i in range(n)]
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return None
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        
        male_a, female_a = self.count[root_a]
        male_b, female_b = self.count[root_b]

        self.count[root_a] = (male_a + male_b, female_a + female_b)
        
        increase = male_a * female_b + male_b * female_a
        return increase

dsu = DSU(N, c)

total_pairs = 0

for a, b in meetings:
    increase = dsu.union(a - 1, b - 1)
    if increase is not None:
        total_pairs += increase
    print(total_pairs)