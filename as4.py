# Course Fee Billing System

# Step 1: Define courses and fees
courses = {
    "Python Programming": 5000,
    "Data Analytics": 8000,
    "AI & ML": 12000
}

# Step 2: Take user input
print("Available Courses:")
for course in courses:
    print(course)

course_name = input("Enter the course name: ")

if course_name in courses:
    original_fee = courses[course_name]
    
    # Step 3: Discounts
    student = input("Are you a student? (yes/no): ").lower()
    early = input("Early registration? (yes/no): ").lower()
    
    discount = 0
    
    if student == "yes":
        discount += 0.10 * original_fee
    if early == "yes":
        discount += 0.05 * original_fee
    
    final_amount = original_fee - discount
    
    # Step 4: Display output
    print("\n--- Billing Details ---")
    print("Course Name       :", course_name)
    print("Original Fee      : ₹", original_fee)
    print("Total Discount    : ₹", discount)
    print("Final Payable Amt : ₹", final_amount)

else:
    print("Invalid course selection!")