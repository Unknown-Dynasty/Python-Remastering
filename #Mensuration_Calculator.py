# Program to Calculate any Measurable Quantity of 3D Figurines
print("Choose Figure")
print("CUbe:1")
print("Cuboid:2")
print("Cylinder:3")
print("Cone:4")
print("Sphere:5")
print("HemiSphere:6")

V1 = int(input("Enter Your Input: "))
if V1 == 1:
    print("Choose Operation")
    print("Volume:1")
    print("TSA:2")
    print("CSA:3")
    X1 = float(input("Enter Length: "))
    Z1 = int(input("Enter Operation: "))
    if Z1 == 1:
     result = X1*X1*X1
     print(f"Result:{result}")
    
    elif Z1 == 2:
        result = 6*X1*X1
        print(f"Result:{result}")
        
    elif Z1 == 3:
        result = 4*X1*X1
        print(f"Result:{result}")
    else:
        print("Invalid Input")

elif V1 == 2:
    print("Choose Operation")
    print("Volume:1")
    print("TSA:2")
    print("CSA:3")
    X1 = float(input("Enter Length: "))
    X2 = float(input("Enter Breadth: "))
    X3 = float(input("Enter Height: "))
    Z1 = int(input("Enter Operation: "))
    if Z1 == 1:
        result = X1*X2*X3
        print(f"Result:{result}")
        
    elif Z1 == 2:
        result = 2*(X1*X2+X2*X3+X1*X3)
        print(f"Result:{result}")
        
    elif Z1 == 3:
        result = 2*(X1+X2)*X3
        print(f"Result:{result}")
        
    else:
        print("Invalid Input")
        
elif V1 == 3:
    print("Choose Operation")
    print("Volume:1")
    print("TSA:2")
    print("CSA:3")
    X1 = float(input("Enter Radius: "))
    X2 = float(input("Enter Height: "))
    Z1 = int(input("Enter Operation: "))
    
    if Z1 == 1:
     result = X1*X2*22/7
     print(f"Result:{result}")
     
    elif Z1 == 2:
        result = 2*22/7*X1(X1+X2)
        print(f"Result:{result}")
        
    elif Z1 == 3:
        result = 2*22/7*X1*X2
        print(f"Result:{result}")
        
    else:
        print("Invalid Input")
        
elif V1 == 4:
    print("Choose Operation")
    print("Volume:1")
    print("TSA:2")
    print("CSA:3")
    X1 = float(input("Enter Radius: "))
    X2 = float(input("Enter Height: "))
    X3 = float(input("Enter the Length: "))
    Z1 = int(input("Enter Operation: "))
    print("Choose Operation")

    
    if Z1 == 1:
        result = 1/3*22/7*X1*X1*X2
        print(f"Result:{result}")
        
    elif Z1 == 2:
        result = 22/7*X1(X3+X1)
        print(f"Result:{result}")

    elif Z1 == 3: 
        result = 22/7*X1*X3
        print(f"Result:{result}")
        
    else:
        print("Invalid Input")
        
elif V1 == 5:
    print("Choose Operation")
    print("Volume:1")
    print("TSA:2")
    X1 = float(input("Enter Radius: "))
    Z1 = int(input("Enter Operation: "))
    
    if Z1 == 1:
        result = 4/3*22/7*X1**(3)
        print(f"Result:{result}")
        
    elif Z1 == 2:
        result = 4*22/7*X1**(2)
        print(f"Result:{result}")
        
    else:
        print("Invalid Input")

elif V1 == 6:      
    print("Choose Operation")
    print("Volume:1")
    print("TSA:2")
    print("CSA:3")
    print("Plane Surface Area")
    X1 = float(input("Enter Radius: "))  
    Z1 = int(input("Enter Operation: "))
    
    if Z1 == 1:
        result = 2/3*22/7*X1**(2)
        print(f"Result:{result}")
        
    elif Z1 == 2:
        result = 3*22/7*X1**(2)
        print(f"Result:{result}")
  
    elif Z1 == 3:
        result = 2*22/7*X1**(2)
        print(f"Result:{result}")
        
    elif Z1 == 4:
        result = 22/7*X1**(2)
        print(f"Result:{result}")
        
    else:
        print("Invalid Input")