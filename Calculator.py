import math


def add(x , y):
    return x + y
def sub(x , y):
    return x - y
def Multi(x , y):
    return x * x
def division(x , y):
    return x / y if y != 0 else "Error: Division by zero"
def sin(x):
    return math.sin(math.radians(x))
def square_root(x):
    return math.sqrt(x)
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def power(x , y):
    return math.pow(x, y)
def cube(x):
    return math.cbrt(x)
def log(x, y):
    return math.log(x, y)
def Constant():
    pi = math.pi          # 3.141592653589793
    e = math.e           # 2.718281828459045
    tau = 2 * pi         # 6.283185307179586
    
    return pi, e, tau
        

def menu():
    print("1. ADDITION ")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. SQUAURE ROOT")
    print("6. SINE")
    print("7. COS")
    print("8. TAN")
    print("9. POWER ")
    print("10. CUBE ROOT")
    print("11. LOGRITHM ")
    

    

while True:
    menu()
    choice = input("Enter choices : 1 - 11:")

    if choice in  ['1','2','3','4','9', '11']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    else:
        num1 = int(input("Enter number correct choice"))

        # Call the right function based on choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", sub(num1, num2))
    elif choice == '3':
        print("Result:", Multi(num1, num2))
    elif choice == '4':
        print("Result:", division(num1, num2))
    elif choice == '5':
        print("Result:", square_root(num1)) 
    elif choice =='6':
        print("Result:", sin(num1))
    elif choice =='7':
        print("Result:" , cos(num1))
    elif choice =='8':
        print("Result :", tan(num1))
    elif choice =='9':
        print("Result:", power(num1, num2))
    elif choice =='10':
        print("Result : ", cube(num1))
    elif choice == '11':
        print("Result : ", log(num1 , num2))
    else :
        print("INVAILD CHOICES")
try:
    num = float(input("Enter number: "))
except ValueError:
    print("Invalid input, please enter a number.")

