import pickle

class Employee:
    def _init_(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

# Serialize
emp = Employee(101, "Alice", "2021-07-15", 50000)
with open("employee.pkl", "wb") as file:
    pickle.dump(emp, file)

# Deserialize
with open("employee.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
    print(vars(loaded_emp))
