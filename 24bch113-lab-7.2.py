import random

random_numbers = {random.randint(15, 45) for _ in range(10)}

count_less_than_30 = sum(1 for number in random_numbers if number < 30)

numbers_to_keep = {number for number in random_numbers if number <= 35}

print("Original set of random numbers:", random_numbers)
print("Count of numbers less than 30:", count_less_than_30)
print("Set after removing numbers greater than 35:", numbers_to_keep)