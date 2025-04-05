my_tuple = (10, 20, 30, 40)

temp_list = list(my_tuple)

temp_list.remove(20)

my_tuple = tuple(temp_list)

print("Tuple after deleting an element:", my_tuple)