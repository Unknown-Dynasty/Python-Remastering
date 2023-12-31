#Prime_Number_Test
numA = int(input("Enter Number: "))
if numA == 1:
    print(f"It is not a Prime Number")
elif numA >1:
    for i in range(2,numA):
        if numA % 1 == 0:
            print(f"It is not a Prime Number")
        else:
            print(f"It is a Prime Number")
    