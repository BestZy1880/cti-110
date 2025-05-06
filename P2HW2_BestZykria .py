# Zykria Best
# 03/15/25
# P2HW2
# This program collects grades for six modules, stores them in a list, and calculates the lowest grade, highest grade, sum of grades, and average.


print("This program calculates statistics for six module grades.\n")

module_grades = []  # List to store grades

module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_grades = sum(module_grades)
average_grade = sum_grades / len(module_grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade:.2f}")
print(f"{'Highest Grade:':<20} {highest_grade:.2f}")
print(f"{'Sum of Grades:':<20} {sum_grades:.2f}")
print(f"{'Average Grade:':<20} {average_grade:.2f}")
print("--------------------------------")
