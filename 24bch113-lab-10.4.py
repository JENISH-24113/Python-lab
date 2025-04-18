str1 = input("Enter the main string: ")
str2 = input("Enter the string to remove: ")
result = ""
i = 0
while i < len(str1):
    if str1[i:i+len(str2)] == str2:
        i += len(str2)
    else:
        result += str1[i]
        i += 1
print("Resulting string after removal:", result)