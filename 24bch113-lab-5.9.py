list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]

list3 = [num for num in list1 if num not in list2]

print("Numbers in the first list but not in the second list:", list3)