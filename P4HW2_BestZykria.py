# Zykria Best
# 04/12/25
# P4HW2 
# This program calculates overtime and regular pay for multiple employees, displays each person's pay breakdown, and prints the total summary at the end.

# Pseudocode:
# 1. Initialize total trackers for regular pay, overtime pay, gross pay, and employee count.
# 2. Use a sentinel loop that continues until the user enters "Done".
# 3. For each employee:
#    - Ask for hours worked and pay rate
#    - Calculate regular hours (up to 40) and overtime (above 40)
#    - Compute regular pay, overtime pay, and gross pay
#    - Display a breakdown of all pay information in a formatted table
#    - Add each to the running totals
# 4. After loop ends, display total employee count and all totals formatted properly

# Initialize totals
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Start sentinel loop
while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name == "Done":
        break

    # Input hours worked and pay rate
    hours = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Determine regular and overtime hours
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours

    # Calculate pay
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Display breakdown
    print()
    print(f"Employee name: {employee_name}")
    print()
    print("Hours Worked  Pay Rate  Overtime  Overtime Pay  RegHour Pay  Gross Pay")
    print(f"{hours:<13.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}"
          f"{overtime_pay:<14.2f}{regular_pay:<13.2f}{gross_pay:<.2f}")
    print()

    # Update totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

# Display final summary
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime   : ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross       : ${total_gross_pay:.2f}")
