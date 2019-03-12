x,y=input()


operation=str(input("Hello there, what is your operation?"))

x = int(x)
y = int(y)

def addition():
    result=x+y
    print(result)

if operation.lower() == "addition":
    addition()