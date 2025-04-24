class Time:
    def __init__(self, h, m): self.h, self.m = h, m
    def add(self, o): return Time(self.h + o.h, self.m + o.m)
    def __str__(self): return f"{self.h} hours {self.m} minutes"

t1, t2 = Time(2, 30), Time(1, 45)
print(t1.add(t2))
