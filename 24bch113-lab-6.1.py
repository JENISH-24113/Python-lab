def count_boys_and_girls(name_list):
    boys_count=0
    girls_count=0

    for name in name_list:
        if isinstance(name,tuple):
            boys_count+=1
        else:
            girls_count+=1
    return boys_count, girls_count

name=[("jenish",),"kiran",("ramesh",),"mahi"]

boys,girls=count_boys_and_girls(name)

print("number of boys:",boys)
print("number of girls:",girls)