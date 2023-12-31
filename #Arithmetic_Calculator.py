# Arithmetic/Exponent_Calculator

print("Arithmetic: 1")
print("Exponent: 2")

A1 = int(input("Enter Choice: "))

if A1 == 1:
    print("Addition:1")
    print("Subtraction:2")
    print("Multiplication:3")
    print("Division:4")
    print("Select Choice")
    
    B1 = float(input("Enter Number 1: "))
    B2 = float(input("Enter Number 2: "))
    C1 = float(input("Enter Operation: "))
    
    if C1 == 1:
        result = B1 + B2
        print(f"Result: {result}")
    elif C1 == 2:
        result = B1 - B2
        print(f"Result: {result}")
    elif C1 == 3:
        result = B1 * B2
        print(f"Result: {result}")
    elif C1 == 4:
        if B2 == 0:
            print("Invalid Input")
        else:
            result = B1 / B2
            print(f"Result: {result}")
    else:
        print("Invalid Input")
        
elif A1 == 2:
    print("Square:1")
    print("Cube:2")
    print("Square Root:3")
    print("Cube Root:4")
    print("Select Choice")
    
    B1 = float(input("Enter Number: "))
    C1 = float(input("Enter Operation: "))
    
    if C1 == 1:
        result = B1 ** 3
        print(f"Result: {result}")
    elif C1 == 2:
        result = B1 ** 2
        print(f"Result: {result}")
    elif C1 == 3:
        result = B1 ** (1/3)
        print(f"Result: {result}")
    elif C1 == 4:
        result = B1 ** 0.5
        print(f"Result: {result}")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")
