class Weather:
    def __init__(self, params): self.params = params
    def __contains__(self, item): return item in self.params

w = Weather(["Rainy", "Sunny", "Cloudy"])
print("Sunny" in w, "Stormy" in w)
