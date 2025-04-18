str1 = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
i = 0
while i < len(str1):
    if str1[i] in vowels:
        count += 1
    i += 1
print("Number of vowels:", count)