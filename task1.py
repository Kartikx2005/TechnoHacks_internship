# Task 1 : Calculator
# Create a basic calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division using functions

def add(a,b):
    return a+b
def subt(a,b):
    if(a>b):
        return a-b
    else:
        return b-a
def multi(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Error! Cannot divide by 0!"
    else:
        return a/b
n = 1
while(n==1):
    print("***********************")
    print("   🖩 CALCULATOR 🖩      ")
    print("***********************")
    a = int(input("Enter the first operand: "))
    b = int(input("Enter the second operand: "))
    op = input("Enter the operator: ")
    if(op=="+" or op=="-" or op=="*" or op=="/"):
        if op == "+":
            r = add(a,b)
            print(r)
        elif op == "-":
            r = subt(a,b)
            print(r)
        elif op == "*":
            r = multi(a,b)
            print(r)
        elif op == "/":
            r = div(a,b)
            print(r)
    else:
        while(op != "+" and op!= "-" and op!= "*" and op!= "/") :
            print("You have entered the wrong operator 😑")
            op = input("Please enter the correct operator: ")
            if op == "+":
                r = add(a,b)
                print(r)
            elif op == "-":
                r = subt(a,b)
                print(r)
            elif op == "*":
                r = multi(a,b)
                print(r)
            elif op == "/":
                r = div(a,b)
                print(r)

    re = input("Do you want to use the calculator again ? (y):🤔 ")
    if(re == 'y' or re == "Y"):
        n = 1
        
    elif(re == 'n' or re == "N"):
        n = 0
        print("Thanks for using our service !😊 ")
    else:
        while(re != "y" and re != "Y" and re != "n" and re != "N"):
            print("You have entered the wrong value!")
            print("Only enter (y or n)")
            if(re == 'y' or re == "Y"):
                n = 1
            elif(re == 'n' or re == "N"):
                n = 0
            print("Thanks for using our service !😊 ")
        
    

