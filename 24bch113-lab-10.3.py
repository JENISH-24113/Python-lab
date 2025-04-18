str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
found = False
i = 0
while i <= len(str1) - len(str2):
    if str1[i:i+len(str2)] == str2:
        found = True
        break
    i += 1
if found:
    print("The second string is present in the first string.")
else:
    print("The second string is not present in the first string.")