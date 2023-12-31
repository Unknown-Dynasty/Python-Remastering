#Distance_Converter     
print("M-Km:1")
print("Km-m:2")
A1 = int(input("Enter Distance: "))
Z1 = int(input("Enter the Choice: "))
if Z1 == 1:
         result = A1/(1.609)
         print(f"Result:{result}")
         
elif Z1 == 2:
         result = A1*(1.609)
         print(f"Result:{result}")
         
else:
         print("Invalid Input")
         