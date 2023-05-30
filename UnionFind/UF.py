class UnionFind():
    def __init__(self, count):
        self.count = count
        self.parent = [i for i in range(count)]

    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])

        return self.parent[x]

    def is_connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def unite(self, p, q):
        rootP = self.find_root(p)
        rootQ = self.find_root(q)
        if rootP != rootQ:
            self.parent[rootP] = rootQ
            self.count -= 1

# todo: test and add comments
uf = UnionFind(5)
