class Complex:
    def __init__(self, r, i):
        self.r, self.i = r, i

    def __add__(self, o): return Complex(self.r + o.r, self.i + o.i)
    def __sub__(self, o): return Complex(self.r - o.r, self.i - o.i)
    def __mul__(self, o): return Complex(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)
    def __truediv__(self, o): 
        d = o.r**2 + o.i**2
        return Complex((self.r * o.r + self.i * o.i) / d, (self.i * o.r - self.r * o.i) / d)

    def __str__(self): return f"{self.r} + {self.i}i"

c1, c2 = Complex(2, 3), Complex(4, 5)
print(c1 + c2, c1 - c2, c1 * c2, c1 / c2)
