class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))  # 1-indexed
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
    
    def findParent(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.findParent(self.parent[u])  # Path compression
        return self.parent[u]

    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)

    def unionByRank(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

    def unionBySize(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
