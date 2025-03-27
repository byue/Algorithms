class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]] # path compression
            x = self.parent[x]
        return x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        rank_x = self.rank[root_x] # use rank to keep tree balanced
        rank_y = self.rank[root_y]
        if rank_x > rank_y:
            self.parent[root_y] = root_x
        elif rank_y > rank_x:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1