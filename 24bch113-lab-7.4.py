names_set = {"Ani", "Brown", "Apple", "banana", "Aamish", "Bob"}

set_a = {name for name in names_set if name.startswith("A")}
set_b = {name for name in names_set if name.startswith("B")}

print("Set of names starting with A:", set_a)
print("Set of names starting with B:", set_b)