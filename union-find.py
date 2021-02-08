class UnionFind:

    '''
    Initialse n sites with integer names 0 to n-1
    '''

    def __init__(self, n):
        self.count = n
        self.id = []
        for i in range(n):
            self.id.append(i)

    '''
    Add connection between p and q
    '''

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        pID = self.id[p]
        qID = self.id[q]

        if pID == qID:
            return
        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
        self.count = self.count - 1

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.id[p] == self.id[q]

    def find(self, p):
        self.validate(p)
        return self.id[p]

    def validate(self, p):
        n = len(self.id)
        if p < 0 or p >= n:
            raise "OutofBoundException"

    def connected(self, p, q):
        pass

    def count(self):
        return self.count


if __name__ == "__main__":
    n = int(input("Enter the length"))
    uf = UnionFind(n)
    while True:
        p = input("Enter p")
        if p == '':
            break
        p = int(p)
        q = int(input("Enter q"))
        if uf.find(p) == uf.find(q):
            continue
        uf.union(p, q)
        print(' is connected to ', p, q)
