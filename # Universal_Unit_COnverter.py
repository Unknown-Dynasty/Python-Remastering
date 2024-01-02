# Universal_Unit_Converter

# Welcoming_User
Name = str(input("Enter Your Name: "))
print(f"Welcome {Name}")

# Printing_Choices_For_User
print("1. Length")
print("2. Mass")
print("3. Volume")
print("4. Area")
print("5. Speed")
print("6. Time")
print("7. Pressure")
print("8. Energy")
print("9. Power")
print("10. Temperature")

# Take_Input_From_Choices
A = int(input("Enter Operation: "))

# Configuration_Of_Different_Inputs
if A == 1:
    print("1. Inch to M")
    print("2. Inch to Cm")
    print("3. M to Km")
    print("4. Mm to Cm")
    print("5. Km to Mile")
    print("6. M to Yard")
    print("7. Mile to Km")
    print("8. Foot to Inch")
    print("9. Inches to Foot")
    print("10. Foot to M")

    B1 = float(input("Enter Length: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1 * 10 ** (4) / 254
        print(f"Result is {result} M")

    elif B2 == 2:
        result = B1 * 10 ** (2) / 254
        print(f"Result is {result} Cm")

    elif B2 == 3:
        result = B1 * 10 ** (3)
        print(f"Result is {result} Km")

    elif B2 == 4:
        result = B1 / 10 ** (2)
        print(f"Result is {result} Cm")

    elif B2 == 5:
        result = B1 * (1.609)
        print(f"Result is {result} Mile")

    elif B2 == 6:
        result = B1 * 5 / 10 ** (4)
        print(f"Result is {result} Yard")

    elif B2 == 7:
        result = B1 / (1.609)
        print(f"Result is {result} Km")

    elif B2 == 8:
        result = B1 * (12)
        print(f"Result is {result} Inch")

    elif B2 == 9:
        result = B1 / (12)
        print(f"Result is {result} Foot")

    elif B2 == 10:
        result = B1 * (3.281)
        print(f"Result is {result} M")

    else:
        print("Invalid Input")

elif A == 2:
    print("1. Kilogram (Kg) to Gram (g)")
    print("2. Kilogram (Kg) to Milligram (Mg)")
    print("3. Gram (g) to Kilogram (Kg)")
    print("4. Milligram (Mg) to Kilogram (Kg)")
    print("5. Pound (Lb) to Kilogram (Kg)")
    print("6. Kilogram (Kg) to Pound (Lb)")
    print("7. Ounce (Oz) to Gram (g)")
    print("8. Gram (g) to Ounce (Oz)")

    B1 = float(input("Enter Mass: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1*10**(3)
        print(f"Result is {result} g")
        
    elif B2 == 2:
        result = B1*10**(6)
        print(f"Result is {result} Mg")
        
    elif B2 == 3:
        result = B1/10**(3)
        print(f"Result is {result} Kg")
        
    elif B2 == 4:
        result = B1/10**(6)
        print(f"Result is {result} Kg") 
        
    elif B2 == 5:
        result = B1*(2.2)
        print(f"Result is {result} Kg")
        
    elif B2 == 6:
        result =B1/(2.2)
        print(f"Result is {result} Lb")
        
    elif B2 == 7:
        result = B1*(28)
        print(f"Result is {result} g")
        
    elif B2 == 8:
        result = B1/(28)
        print(f"Result is {result} Oz")
        
    else:
        print("Invalid Input")

elif A == 3:
    print("1. Liter (L) to Milliliter (mL)")
    print("2. Milliliter (mL) to Liter (L)")
    print("3. Cubic Meter (m³) to Liter (L)")
    print("4. Cubic Meter (m³) to Milliliter (mL)")
    print("5. Gallon (US) to Liter (L)")
    print("6. Liter (L) to Gallon (US)")
    
    B1 = float(input("Enter Volume: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1*10**(3)
        print(f"Result is {result} mL")
        
    elif B2 == 2:
        result = B1/10**(3)
        print(f"Result is {result} L")
        
    elif B2 == 3:
        result = B1*10**(3)
        print(f"Result is {result} L")
        
    elif B2 == 4:
        result = B1*10**(6)
        print(f"Result is {result} mL")
        
    elif B2 == 5:
        result = B1*(3.785)
        print(f"Result is {result} L")
        
    elif B2 == 6:
        result = B1/(3.785)
        print(f"Result is {result} G")
        
    else:
        print("Invalid Input")
        
elif A == 4:
    print("1. Square Meter (m²) to Square Kilometer (km²)")
    print("2. Square Kilometer (km²) to Square Meter (m²)")
    print("3. Square Mile (mi²) to Square Kilometer (km²)")
    print("4. Square Kilometer (km²) to Square Mile (mi²)")
    print("5. Acre to Square Meter (m²)")
    print("6. Square Meter (m²) to Acre")
    
    B1 = float(input("Enter Area: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1*10**(6)
        print(f"Result is {result} km2")
        
    elif B2 == 2:
        result = B1*10**(6)
        print(f"Result is {result} m2")
        
    elif B2 == 3:
        result = B1/(2.59)
        print(f"Result is {result} km2")
        
    elif B2 == 4:
        result = B1*(2.59)
        print(f"Result is {result} mi2")
        
    elif B2 == 5:
        result = B1*(4046.86)
        print(f"Result is {result} m2")
        
    elif B2 == 6:
        result = B1/(4046.86)
        print(f"Result is {result} Acre")

    else:
        print("Invalid Input")    
elif A == 5:
    print("1. Meter/Second (m/s) to Kilometer/Hour (km/h)")
    print("2. Kilometer/Hour (km/h) to Meter/Second (m/s)")
    print("3. Mile/Hour (mi/h) to Kilometer/Hour (km/h)")
    print("4. Knot (kn) to Kilometer/Hour (km/h)")

    B1 = float(input("Enter Speed: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1 * 3.6
        print(f"Result is {result} km/h")

    elif B2 == 2:
        result = B1 / 3.6
        print(f"Result is {result} m/s")

    elif B2 == 3:
        result = B1 * 1.609
        print(f"Result is {result} km/h")

    elif B2 == 4:
        result = B1 * 1.852
        print(f"Result is {result} km/h")

    else:
        print("Invalid Input")

elif A == 6:
    print("1. Second (s) to Minute (min)")
    print("2. Minute (min) to Second (s)")
    print("3. Hour (hr) to Minute (min)")
    print("4. Day to Hour (hr)")
    print("5. Week to Day")
    print("6. Month to Day")
    print("7. Year to Day")

    B1 = float(input("Enter Time: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1 / 60
        print(f"Result is {result} min")

    elif B2 == 2:
        result = B1 * 60
        print(f"Result is {result} s")

    elif B2 == 3:
        result = B1 * 60
        print(f"Result is {result} min")

    elif B2 == 4:
        result = B1 * 24
        print(f"Result is {result} hr")

    elif B2 == 5:
        result = B1 * 7
        print(f"Result is {result} Day")

    elif B2 == 6:
        result = B1 * 30
        print(f"Result is {result} Day")

    elif B2 == 7:
        result = B1 * 365
        print(f"Result is {result} Day")

    else:
        print("Invalid Input")

elif A == 7:
    print("1. Pascal (Pa) to Kilopascal (kPa)")
    print("2. Kilopascal (kPa) to Pascal (Pa)")
    print("3. Megapascal (MPa) to Kilopascal (kPa)")
    print("4. Bar (bar) to Pascal (Pa)")
    print("5. Atmosphere (atm) to Pascal (Pa)")

    B1 = float(input("Enter Pressure: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1 * 10 ** 3
        print(f"Result is {result} kPa")

    elif B2 == 2:
        result = B1 / 10 ** 3
        print(f"Result is {result} Pa")

    elif B2 == 3:
        result = B1 / 10 ** 3
        print(f"Result is {result} kPa")

    elif B2 == 4:
        result = B1 * 10 ** 5
        print(f"Result is {result} Pa")

    elif B2 == 5:
        result = B1 * 10 ** 5
        print(f"Result is {result} Pa")

    else:
        print("Invalid Input")

elif A == 8:
    print("1. Joule (J) to Kilojoule (kJ)")
    print("2. Kilojoule (kJ) to Megajoule (MJ)")
    print("3. Kilocalorie (kcal) to Kilojoule (kJ)")
    print("4. Electronvolt (eV) to Kilojoule (kJ)")

    B1 = float(input("Enter Energy: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1 * 10 ** 3
        print(f"Result is {result} kJ")

    elif B2 == 2:
        result = B1 * 10 ** 6
        print(f"Result is {result} MJ")

    elif B2 == 3:
        result = B1 * 0.23
        print(f"Result is {result} kJ")

    elif B2 == 4:
        result = B1 * 6 * 10 ** 21
        print(f"Result is {result} kJ")

    else:
        print("Invalid Input")
elif A == 9:
    print("1. Watt (W) to Kilowatt (kW)")
    print("2. Kilowatt (kW) to Megawatt (MW)")
    print("3. Horsepower (hp) to Kilowatt (kW)")
    print("4. Kilowatt (kW) to Horsepower (hp)")

    B1 = float(input("Enter Power: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = B1 / 10 ** 3
        print(f"Result is {result} kW")

    elif B2 == 2:
        result = B1 / 10 ** 3
        print(f"Result is {result} MW")

    elif B2 == 3:
        result = B1 / 0.7457
        print(f"Result is {result} kW")

    elif B2 == 4:
        result = B1 * 0.7457
        print(f"Result is {result} hp")

    else:
        print("Invalid Input")

elif A == 10:
    print("1. Celsius (°C) to Fahrenheit (°F)")
    print("2. Fahrenheit (°F) to Celsius (°C)")

    B1 = float(input("Enter Temperature: "))
    B2 = int(input("Enter Choice: "))

    if B2 == 1:
        result = (B1 * 9/5) + 32
        print(f"Result is {result} °F")

    elif B2 == 2:
        result = (B1 - 32) * 5/9
        print(f"Result is {result} °C")

    else:
        print("Invalid Input")
