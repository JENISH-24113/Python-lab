physics=int(input("Enter your mark:"))
chemistry=int(input("Enter your mark:"))
biology=int(input("Enter your mark:"))

Avg=physics+chemistry+biology/3

if(Avg>=80):
    print("Distinction")
elif(Avg>=60 or Avg<80):
    print("First division")
elif(Avg>=45 or Avg<60):
    print("Second division")
elif(Avg>=40 or Avg<45):
    print("Pass")
elif(Avg<40):
    print("Promotion not granted")