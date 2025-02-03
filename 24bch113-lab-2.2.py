a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the third value:"))
#largest value:
if(a>b and a>c):
    print("a is the largest:")
elif(b>c and b>a):
    print("b is the largest:")
else:
    print("c is the largest:")
#smallest value:
if(a<b and a<c):
    print("a is the smallest:")
elif(b<c and b<a):
    print("b is the smallest:")
else:
    print("c is the smallest:")

