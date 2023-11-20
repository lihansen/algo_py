

class union_find:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]


    def find_root(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self, x)

        return self.parent[x];