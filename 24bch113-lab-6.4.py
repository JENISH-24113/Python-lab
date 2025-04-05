food_items = [
    ("Pizza", 300),
    ("Burger", 150),
    ("Pasta", 250),
    ("Salad", 120),
    ("Sushi", 400)]


sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)


print("Food items sorted by price (descending order):")
for item in sorted_items:
    print(f"{item[0]}: {item[1]}")