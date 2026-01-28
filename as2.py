emp_name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
basic_salary = float(input("Enter your Basic Salary: "))

hra = 0.20 * basic_salary
da = 0.10 * basic_salary
pf = 0.12 * basic_salary

net_salary = basic_salary + hra + da - pf

print("\n--- Salary Summary ---")
print("Employee Name:", emp_name)
print("Employee ID:", emp_id)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("Net Salary:", net_salary)

