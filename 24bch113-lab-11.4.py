class Shape:
    def __init__(self, s): self.s = s
    def perimeter(self): return 4 * self.s
    def area(self): return self.s**2

sq = Shape(4)
print(sq.perimeter(), sq.area())
