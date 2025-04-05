def separate_details(student_list):
    roll_numbers = []
    names = []
    ages = []

    for student in student_list:
        roll_numbers.append(student[0])
        names.append(student[1])
        ages.append(student[2])
    
    return roll_numbers, names, ages

students = [
    (101, "John", 20),
    (102, "Emily", 22),
    (103, "Mike", 21),
    (104, "Sophia", 23)
]

roll_numbers, names, ages = separate_details(students)

print("Roll Numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)