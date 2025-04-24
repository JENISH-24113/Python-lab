class Matrix:
    def __init__(self, m): self.m = m
    def add(self, o): return [[self.m[i][j] + o.m[i][j] for j in range(3)] for i in range(3)]
    def multiply(self, o): return [[sum(self.m[i][k] * o.m[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    def transpose(self): return [[self.m[j][i] for j in range(3)] for i in range(3)]

m1, m2 = Matrix([[1,2,3],[4,5,6],[7,8,9]]), Matrix([[9,8,7],[6,5,4],[3,2,1]])
print(m1.add(m2), m1.multiply(m2), m1.transpose())
