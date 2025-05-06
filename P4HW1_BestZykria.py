# Zykria Best
# 04/12/25
# P4HW1 
# This program asks the user how many scores they want to enter, takes the scores with validation, drops the lowest one, calculates the average of the rest, and displays the letter grade.

# Pseudocode:
# 1. Ask user for number of scores to enter
# 2. Create an empty list to store the scores
# 3. Loop to collect valid scores (between 0 and 100)
#    - If invalid, display error and re-ask
# 4. Drop the lowest score from the list
# 5. Calculate the average of the remaining scores
# 6. Determine the letter grade based on the average
# 7. Display:
#    - Lowest score
#    - Modified list (after dropping lowest)
#    - Average (2 decimal places)
#    - Letter grade

# Get number of scores from user
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store scores
scores = []

# Loop to collect valid scores
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i + 1} again:")

# Drop the lowest score
lowest_score = min(scores)
scores.remove(lowest_score)

# Calculate average of remaining scores
average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display formatted results
print("\n--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")
