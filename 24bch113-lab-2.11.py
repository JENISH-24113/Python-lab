x1=float(input("Enter the first point:"))
x2=float(input("Enter the second point:"))
x3=float(input("Enter the third point:"))
y1=float(input("Enter the fourth point:"))
y2=float(input("Enter the fifth point:"))
y3=float(input("Enter the sixth point:"))

d=y3-y2/x3-x2 == y2-y1/x2-x1

if(d):
    print("three points fall on the straight line:")
else:
    print("three point not fall on the sttraight line:")