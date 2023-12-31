#Temperature_COnverter
        
print("Select Method")
print("C to F:1")
print("F to C:2")
     
A1 = float(input("Enter Degree: "))
Z1 = float(input("Enter Choice: "))
if Z1 == 1:
        result = (9/5)*A1+32
        print(f"Result:{result}")
elif Z1 == 2:
        result = (5/9)*(A1-32)
        print(f"Result:{result}")
else:
        print("Invalid Input")    
