str1 = input("Enter a string: ")
lower_result = ""
upper_result = ""
toggle_result = ""
i = 0

while i < len(str1):
    char = str1[i]
    
    # Convert to lower case
    if 'A' <= char <= 'Z':
        lower_result += chr(ord(char) + 32)
    else:
        lower_result += char
    
    # Convert to upper case
    if 'a' <= char <= 'z':
        upper_result += chr(ord(char) - 32)
    else:
        upper_result += char
    
    # Convert to toggle case
    if 'a' <= char <= 'z':
        toggle_result += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        toggle_result += chr(ord(char) + 32)
    else:
        toggle_result += char
    
    i += 1

print("Lower case string:", lower_result)
print("Upper case string:", upper_result)
print("Toggle case string:", toggle_result)