class Date:
    def __init__(self, d, m, y): self.d, self.m, self.y = d, m, y
    def __eq__(self, o): return (self.d, self.m, self.y) == (o.d, o.m, o.y)

d1, d2 = Date(15, 4, 2025), Date(15, 4, 2025)
print(d1 == d2)
