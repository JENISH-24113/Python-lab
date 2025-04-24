class Solid:
    def __init__(self, r, h): self.r, self.h = r, h
    def surface_area(self): return 2 * 3.14 * self.r * (self.r + self.h)
    def volume(self): return 3.14 * self.r**2 * self.h

s = Solid(3, 5)
print(s.surface_area(), s.volume())
