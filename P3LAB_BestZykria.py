# Zykria Best
# 03/25/25
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make up a given amount of money. It omits any coin not needed and uses singular/plural correctly.

amount = float(input("Enter the amount of money as a float: $"))

cents = int(round(amount * 100))

dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

if dollars == quarters == dimes == nickels == pennies == 0:
    print("No change")
else:
    if dollars:
        print(f"{dollars} Dollar" + ("s" if dollars > 1 else ""))
    if quarters:
        print(f"{quarters} Quarter" + ("s" if quarters > 1 else ""))
    if dimes:
        print(f"{dimes} Dime" + ("s" if dimes > 1 else ""))
    if nickels:
        print(f"{nickels} Nickel" + ("s" if nickels > 1 else ""))
    if pennies:
        print(f"{pennies} Penn" + ("ies" if pennies > 1 else "y"))
