# Zykria Best
# 02/28/25
# P1HW1
#This program takes user input, calculates the power, and then performs an addition and subtraction operation based on user input.


print("-----Calculating Exponents-----\n")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

print("-----Addition and Subtraction-----\n")

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(f"\n{num1} + {num2} - {num3} is equal to {final_result}\n")
