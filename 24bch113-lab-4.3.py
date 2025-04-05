str1 = input("Enter the main string: ")
str2 = input("Enter the string to search for: ")
def check_string(str1,str2):
    if str2 in str1:
        print("str2 is present in str1")
    else:
        print("str2 is not present in str1")

check_string(str1,str2);         
    