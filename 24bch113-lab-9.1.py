import csv

data = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3"],
    [1, "Alice", 85, 90, 88],
    [2, "Bob", 78, 82, 80]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created successfully.")