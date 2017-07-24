import math

def calculator(no1, no2, option):
    print(no1, no2, option)
    if option == '2':
        print("Adding the two numbers")
        return no1 + no2
    elif (option == '3'):
        print("Dividing the two numbers")
        if no2 != 0:
            result = no1 / no2
        else:
            result = float('Inf')
        return result
    elif (option == '4'):
        print("Power function in math")
        result = pow(no1,no2)
        return result
    else:
        print("Enter valid option")
        return 
    

option_exit = False

while(option_exit is False):
    print("Enter two numbers:")
    no1, no2 = map(int, input().split())
    print("1. Help \n2. Add \n3. Divide \n4. Power function \n5. Quit calculator")
    option = input("Enter your option:")
    if(option == '1'):
       help()
    elif (option == '5'):
        option_exit = True
    else:
        result = calculator(no1, no2, option)
        print("Result: ", result)
    
    
