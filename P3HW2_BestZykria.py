# Zykria Best
# 03/30/25
# P3HW2 
# This program asks for employee information, calculates overtime, regular pay, and gross pay, then displays a formatted breakdown of all the amounts.


employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

print("----------------------------------------")
print(f"Employee name:  {employee_name}")
print()
print("Hours Worked  Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-------------------------------------------------------------------------------")
print(f"{hours_worked:<13.1f}{pay_rate:<11.1f}{overtime_hours:<11.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
