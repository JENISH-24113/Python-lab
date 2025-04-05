tuples_list = [("Apple", 50), (), ("Banana", 30), (), ("Cherry", 20)]

filtered_list = [tup for tup in tuples_list if tup]

print("List after removing empty tuples:", filtered_list)