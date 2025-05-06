# Zykria Best
# 02/22/2025
# P2LAB2
#This program creates a dictionary with vehicles and their MPG values, displays the available vehicles, and when selected, calculates the gallons of gas needed for a given number of miles

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

print(vehicles.keys())

selected_vehicle = input("\nEnter a vehicle to see its mpg: ")

if selected_vehicle in vehicles:
    mpg = vehicles[selected_vehicle]
    print(f"\nThe {selected_vehicle} gets {mpg:.2f} mpg.")

    miles = float(input(f"\nHow many miles will you drive the {selected_vehicle}? "))

    gallons_needed = miles / mpg

    print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {selected_vehicle} {miles:.1f} miles.")
else:
    print("\nError: Vehicle not found. Please enter a valid vehicle from the list.")
