
# Zykria Best
# 03/15/25
# P2HW1
# This program takes user input for a budget and travel expenses, calculates total expenses, and displays the remaining balance in a well-formatted manner.


print("This program calculates and displays travel expenses\n")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_cost = float(input("How much do you think you will spend on gas? "))
hotel_cost = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_cost = float(input("Last, how much do you need for food? "))


total_expenses = gas_cost + hotel_cost + food_cost
remaining_budget = budget - total_expenses


print("\n------------Travel Expenses------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas_cost:,.2f}")
print(f"{'Accommodation:':<20} ${hotel_cost:,.2f}")
print(f"{'Food:':<20} ${food_cost:,.2f}")
print("--------------------------------------")
print(f"{'Remaining Balance:':<20} ${remaining_budget:,.2f}")
