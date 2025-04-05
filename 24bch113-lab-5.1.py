import random


odd_integers = [random.randint(1, 100) | 1 for _ in range(5)]  
print("List of 5 odd integers created:", odd_integers)


even_integers = [random.randint(1, 100) & ~1 for _ in range(4)] 
print("List of 4 even integers created:", even_integers)


odd_integers[2] = even_integers
print("Updated odd integers list after replacing third element:", odd_integers)


flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)


sorted_list = sorted(flattened_list)
print("Sorted list:", sorted_list)