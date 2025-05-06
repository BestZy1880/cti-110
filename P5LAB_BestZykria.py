# Zykria Best 
# 04/20/25
# P5LAB
# This program simulates a self-checkout machine. It calculates the change owed to a customer and displays the number of coins and dollars required to make that change.

import random

def disperse_change(change):
    # Convert change to cents
    change_cents = int(round(change * 100))

    dollars = change_cents // 100
    change_cents %= 100

    quarters = change_cents // 25
    change_cents %= 25

    dimes = change_cents // 10
    change_cents %= 10

    nickels = change_cents // 5
    change_cents %= 5

    pennies = change_cents

    # Print change breakdown
    if dollars > 0:
        print(f"\n{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"\nYou owe ${amount_owed}")

    cash = float(input("How much cash will you put in the self-checkout? "))
    
    if cash < amount_owed:
        print("That's not enough money. Transaction canceled.")
    else:
        change = round(cash - amount_owed, 2)
        print(f"Change is: ${change:.2f}")
        disperse_change(change)

# Call main function
main()
