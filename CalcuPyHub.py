print("<--------------------------Welcome to the calculator!-------------------------->")

import math
def add(x, y):
    return (x+y)

def subtract(x, y):
    return (x-y)

def multiply(x, y):
    return (x*y)

def division(x, y):
    if y != 0:
        return (x/y)
    
def square(a):
    return (a*a)

def cube(a):
    return(a*a*a)

def percentage(a, b):
    return (a/b) * 100

def modulus(a, b):
    return (a%b)

def square_root(a):
    return math.sqrt(a)

def cube_root(a):
    return a**(1/3)

#Calculator main program loop
while True:
    print("\n\n\n\n            What would you like to do? \n")
    print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Square\n\n6.Cube 7.Percentage 8.Modulus 9.Suare Root 10.Cube Root")
    print('''\n                     11.Exit\n\n\n\n
*********************************************************************************\n''')

    choice = input("Enter your choice (1-11): ")

    if choice == '11':
        print("Exiting the program...")
        break

   

    if choice == '1':
        print("\n       #Addition")
        num1 = float(input("\nEnter the 1st number: "))
        num2 = float(input("\nEnter the 2nd number: "))
        print("\nAddition ",num1,"+",num2,"=",add(num1, num2))
        print("\n*********************************************************************************")
    elif choice == '2':
        print("\n    #Subtraction")
        num1 = float(input("\nEnter the 1st number: "))
        num2 = float(input("\nEnter the 2nd number: "))
        print("\nSubtraction ",num1,"-",num2,"=", subtract(num1, num2))
        print("\n*********************************************************************************")
    elif choice == '3':
        print("\n   #Multiplication")
        num1 = float(input("\nEnter the 1st number: "))
        num2 = float(input("\nEnter the 2nd number: "))
        print("\nMultiplication ",num1,"x",num2,"=", multiply(num1, num2))
        print("\n*********************************************************************************")
    elif choice == '4':
        print("\n      #Division")
        num1 = float(input("\nEnter the 1st number: "))
        num2 = float(input("\nEnter the 2nd number: "))
        print("\nDivision ",num1,"/",num2,"=",division(num1, num2))
        print("\n*********************************************************************************")
    elif choice == '5':
        print("\n             #Square")
        num=float(input("\nEnter the Number to finding Square: "))
        print("\nSquare ",num,"X",num,"=",square(num))
        print("\n*********************************************************************************")
    elif choice == '6':
        print("\n            #Cube")
        num=float(input("\nEnter the Number to finding Cube: "))
        print("\nCube ",num,"X",num,"X",num,"=",cube(num))
        print("\n*********************************************************************************")
    elif choice == '7':
        print("\n      #Percentage")
        num1 = float(input("\nEnter the Given number: "))
        num2 = float(input("\nEnter the Total number: "))
        print("\nPercentage (",num1,"/",num2,") X 100 =",percentage(num1, num2),"%")
        print("\n*********************************************************************************")
    elif choice == '8':
        print("\n      #Modulus")
        num1 = float(input("\nEnter the 1st number: "))
        num2 = float(input("\nEnter the 2nd number: "))
        print("\nModulus ",num1,"%",num2,"=", modulus(num1, num2))
        print("\n*********************************************************************************")
    elif choice == '9':
        print("\n           #Square Root")
        num=float(input("\nEnter the Number to finding Square Root: "))
        print("\nSquare Root of",num,"is", square_root(num))
        print("\n*********************************************************************************")
    elif choice == '10':
        print("\n            #Cube Root")
        num = float(input("\nEnter the Number to finding Cube Root: "))
        print("\nCube Root of",num,"is", cube_root(num))
        print("\n*********************************************************************************")
    else:
        print("\nInvalid input. Please try again.")
        print("\n*********************************************************************************")
