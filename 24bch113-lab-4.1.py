str= input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for char in str:
    if char in vowels:
        vowel_count += 1

print("The number of vowels in the string is:",vowel_count)

