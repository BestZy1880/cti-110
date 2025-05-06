# Zykria best
# 4/05/25
# P4LAB2 Multiplication Table Program


repeat = "yes"

while repeat.lower() == "yes":
    number = int(input("Enter an integer: "))

    if number >= 0:
        print(f"\nMultiplication table for {number}")
        print("---------------------------")
        for i in range(1, 13):  # 1 through 12
            print(f"{number} x {i} = {number * i}")
    else:
        print("Sorry, I cannot accept negative values.")

    # Ask to run again
    repeat = input("\nDo you want to run the program again? (yes/no): ")
    
print("Goodbye!")
