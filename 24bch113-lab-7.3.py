names_set = set()

names_set.update(["mihir", "prince", "jenish", "smit", "suresh"])
print("Set after adding five names:", names_set)

if "smit" in names_set:
    names_set.remove("smit")
    names_set.add("raj")
print("Set after modifying one name:", names_set)

names_set.discard("mihir")  
names_set.discard("suresh")
print("Set after deleting two names:", names_set)