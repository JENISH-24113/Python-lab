my_tuple = (10, 20, 30, 40)

temp_list = list(my_tuple)

temp_list[1] = 25

my_tuple = tuple(temp_list)

print("Modified tuple:", my_tuple)