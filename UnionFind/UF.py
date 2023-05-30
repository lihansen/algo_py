class UnionFind:
    def __init__(self, count):
        self.count = count
        self.parent = [i for i in range(count)]  # initially, every node directly point to its root

    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])  # compress the path; find the root and every node
            # in the tree connect to the root directly

        return self.parent[x]

    def is_connected(self, p, q):
        return self.find_root(p) == self.find_root(q)  # same root

    def unite(self, p, q):
        rootP = self.find_root(p)
        rootQ = self.find_root(q)

        if rootP != rootQ:
            self.parent[rootP] = rootQ  # merge tree p to tree q by connect the root to another
            self.count -= 1

    def __str__(self):
        return str(self.parent)


uf = UnionFind(5)
print(uf)
uf.unite(0, 1)
print(uf)
uf.unite(1, 2)
print(uf)

uf.unite(3, 4)
print(uf)

uf.unite(2, 4)
print(uf)
