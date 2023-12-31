# Universal Distance Converter
print("Km - Au")
print("Au-Ly")
print("Ly - Km")
A1 = int(input("Enter Choice: "))
if A1 == 1:
   B1 = float(input("Enter Km: "))
   result =  B1/(149597870.7)
   print(f"Result:{result}")
elif A1 == 2:
    B2 = float(input("Enter AU: "))
    result = B2/(63241.1)
    print(f"Result:{result}")
elif A1 == 3:
    B3 = float(input("Enter LY: "))
    result = B3*(9.641*10**(12))
    print(f"Result:{result}")
else:
    print("Invalid Input")