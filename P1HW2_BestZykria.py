# Zykria Best
# 03/01/25
# P1HW2
# This program takes user input, calculates total expenses, and displays the remaining balance.

print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_cost = float(input("How much do you think you will spend on gas? "))
hotel_cost = float(input("Approximately how much will you need for accommodation/hotel? "))
food_cost = float(input("Last, how much do you need for food? "))

total_expenses = gas_cost + hotel_cost + food_cost
remaining_budget = budget - total_expenses

print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget:.2f}\n")
print(f"Fuel: {gas_cost:.2f}")
print(f"Accommodation: {hotel_cost:.2f}")
print(f"Food: {food_cost:.2f}\n")
print(f"Remaining Balance: {remaining_budget:.2f}")

