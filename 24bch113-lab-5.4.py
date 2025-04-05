def fun():
    print("This is the fun() function")

def disp():
    print("This is the disp() function")

def msg():
    print("This is the msg() function")

functions_list = [fun, disp, msg]

for func in functions_list:
    func()