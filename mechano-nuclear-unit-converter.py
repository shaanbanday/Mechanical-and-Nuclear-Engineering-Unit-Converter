def length_conversion():
    print("\nLength Conversions:")
    print("a) Meters to Feet")
    print("b) Feet to Meters")
    print("c) Inches to Centimeters")
    print("d) Centimeters to Inches")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value * 3.28084,  # m to ft
        'b': value / 3.28084,  # ft to m
        'c': value * 2.54,     # in to cm
        'd': value / 2.54      # cm to in
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def mass_conversion():
    print("\nMass Conversions:")
    print("a) Kilograms to Pounds")
    print("b) Pounds to Kilograms")
    print("c) Grams to Ounces")
    print("d) Ounces to Grams")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value * 2.20462,  # kg to lb
        'b': value / 2.20462,  # lb to kg
        'c': value / 28.3495,  # g to oz
        'd': value * 28.3495   # oz to g
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def pressure_conversion():
    print("\nPressure Conversions:")
    print("a) kPa to psi")
    print("b) psi to kPa")
    print("c) kPa to bar")
    print("d) bar to kPa")
    print("e) kPa to atm")
    print("f) atm to kPa")
    print("g) bar to atm")
    print("h) atm to bar")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value * 0.145038,  # kPa to psi
        'b': value / 0.145038,  # psi to kPa
        'c': value / 100,       # kPa to bar
        'd': value * 100,       # bar to kPa
        'e': value / 101.325,   # kPa to atm
        'f': value * 101.325,   # atm to kPa
        'g': value / 1.01325,   # bar to atm
        'h': value * 1.01325    # atm to bar
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def energy_conversion():
    print("\nEnergy Conversions:")
    print("a) Joules to kWh")
    print("b) kWh to Joules")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value / 3.6e6,  # J to kWh
        'b': value * 3.6e6   # kWh to J
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def power_conversion():
    print("\nPower Conversions:")
    print("a) Watts to Horsepower")
    print("b) Horsepower to Watts")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value / 745.7,  # W to hp
        'b': value * 745.7   # hp to W
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def torque_conversion():
    print("\nTorque Conversions:")
    print("a) Newton-meters to Foot-pounds")
    print("b) Foot-pounds to Newton-meters")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value * 0.737562,  # Nm to ft-lbf
        'b': value / 0.737562   # ft-lbf to Nm
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def radiation_conversion():
    print("\nRadiation Dose Conversions:")
    print("a) Sieverts to REM")
    print("b) REM to Sieverts")
    print("c) Roentgen to Sieverts")
    print("d) Sieverts to Roentgen")
    print("e) REM to Roentgen")
    print("f) Roentgen to REM")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value * 100,    # Sv to REM
        'b': value / 100,    # REM to Sv
        'c': value * 0.009,  # R to Sv
        'd': value / 0.009,  # Sv to R
        'e': value / 0.009,  # REM to R
        'f': value * 0.009   # R to REM
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def radioactivity_conversion():
    print("\nRadioactivity Conversions:")
    print("a) Becquerel to Curie")
    print("b) Curie to Becquerel")
    choice = input("Select an option: ")
    value = float(input("Enter value: "))
    
    conversions = {
        'a': value / 3.7e10,  # Bq to Ci
        'b': value * 3.7e10   # Ci to Bq
    }
    
    print("Converted value:", conversions.get(choice, "Invalid option"))

def main():
    while True:
        print("\nMain Menu:")
        print("1) Length")
        print("2) Mass")
        print("3) Pressure")
        print("4) Energy")
        print("5) Power")
        print("6) Torque")
        print("7) Radiation Dose")
        print("8) Radioactivity")
        print("9) Exit")
        choice = input("Select a category: ")
        
        functions = {
            '1': length_conversion,
            '2': mass_conversion,
            '3': pressure_conversion,
            '4': energy_conversion,
            '5': power_conversion,
            '6': torque_conversion,
            '7': radiation_conversion,
            '8': radioactivity_conversion,
            '9': exit
        }
        
        functions.get(choice, lambda: print("Invalid choice"))()
        
main()
