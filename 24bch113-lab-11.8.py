class String:
    def __init__(self, s): self.s = s
    def __iadd__(self, o): self.s += o.s; return self
    def toLower(self): return self.s.lower()
    def toUpper(self): return self.s.upper()

s1, s2 = String("Hello"), String(" World")
s1 += s2
print(s1.s, s1.toLower(), s1.toUpper())
