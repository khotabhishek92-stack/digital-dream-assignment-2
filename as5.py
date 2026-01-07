# Employee Bonus Evaluation System

# Step 1: Input
employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
rating = int(input("Enter Performance Rating (1-5): "))

# Step 2: Bonus Calculation
bonus = 0

if rating == 5:
    bonus = 0.20 * salary
elif rating == 4:
    bonus = 0.15 * salary
elif rating == 3:
    bonus = 0.10 * salary
else:
    bonus = 0

final_salary = salary + bonus

# Step 3: Display Output
print("\n--- Bonus Evaluation Result ---")
print("Employee Name     :", employee_name)
print("Performance Rating:", rating)
print("Bonus Amount      : ₹", bonus)
print("Final Salary      : ₹", final_salary)