while True:
    full_name = input("Enter your full name (letters only, max 30 characters): ")

    if len(full_name) == 0: #Name field should not be empty
        print("Invalid name. Full Name cannot be empty.")
    elif not full_name.isalpha():# No restricted characters or numbers
        print("Invalid name. Please use letters only (no spaces, numbers, or symbols).")
    elif len(full_name) > 30:#Assming that length of the name cannot exceed 30 characters,I would add space later
        print("Invalid name. Please keep it under 30 characters.")
    else:
        break  # input is valid

print("Student\'s full name:", full_name)

while True:
    try:
        age = int(input("Enter your age : "))
        if  0 < age < 18:#Age cannot be less than 0
            print(full_name + " you are a Primary School Student.")
        elif  18 <= age <= 65:#Assuming that 65 is the age limit for the college
            print(full_name + " you are a College Student.")
            break
        else:
            print("Age is out of range.Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        avg_grade_previous = float(input("Enter your average grade for the previous year: "))
        avg_grade_current = float(input("Enter your average grade for the current year: "))

        # User should not be able to enter negative input,as it can  end up in a positive sum
        if avg_grade_previous < 0 or avg_grade_current < 0:
            print("Grades cannot be negative. Please enter valid numbers.")
            continue

        avg_years = (avg_grade_current + avg_grade_previous) / 2

        if avg_years <= 50:
            print("You failed.")
        else:
            print("You passed.")
        break  # Exit the loop after successful input and result
    except ValueError:
        print("Invalid input. Please enter a valid number.")

