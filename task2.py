# Task 1 : Temperature Convertor
# Create a program that allows the user to convert temperatures between Fahrenheit and Celsius.
n = 1
while n == 1: 
    print("*****Temperature Convertor***** ❄️")
    print("****Welcome to our Service**** 🤝")
    print("1. Celcius to Farenhiet 🔥")
    print("2. Farenhiet to Celcius ❄️")
    c = int (input("Enter your choice : 🤔 "))
    if(c==1):
        celsius = float(input("Enter the temperature in Celcius : ℃ "))
        farenhiet = (celsius * 9/5) + 32
        print("The temperature in Farenhiet is : ",farenhiet, "℉")
    elif(c==2):
        farenhiet = float(input("Enter the temperature in Farenhiet : ℉ "))
        celsius = (farenhiet - 32) * 5/9
        print("The temperature in Celcius is : ",celsius, "℃")
    else:
        print("Invalid Choice 😔")
    
    re = input("Do you want to use the service again? (y or n) 🤔 ")
    if re == 'y':
        n = 1
    else:
        n = 0
        print("Thank you for using our service ! 👋")

