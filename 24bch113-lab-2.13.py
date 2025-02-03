num=int(input("Enter a number (0to19):"))
def number_to_word(num):
    number_words = [
        "zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    
    if 0 <= num <= 19:
        print(number_words[num])
    else:
        print("Number out of range.")

    print("number of word:",number_words(num))    

        

