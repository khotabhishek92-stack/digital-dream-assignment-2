# Intern Data Validation System

name = input("Enter Intern Name: ")
age = int(input("Enter Age: "))
email = input("Enter Email ID: ")
contact = input("Enter Contact Number: ")
percentage = float(input("Enter Graduation Percentage: "))

if age < 18:
    print("Rejected: Age must be 18 or above")

elif percentage < 60:
    print("Rejected: Graduation percentage must be 60% or above")

elif len(contact) != 10 or not contact.isdigit():
    print("Rejected: Contact number must contain exactly 10 digits")

else:
    print("Intern Eligible for Internship")
