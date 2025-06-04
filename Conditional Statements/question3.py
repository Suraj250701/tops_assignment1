# Write a Python program to calculate grades based on percentage using if-else ladder.

usr_input = int(input("Enter your percentage: "))
if usr_input < 0 or usr_input > 100:
    print("Invalid input. Please enter a percentage between 0 and 100.")
elif usr_input >= 90 and usr_input <= 100:
    print("Grade: A")
elif usr_input >= 80 and usr_input < 90:
    print("Grade: B")
elif usr_input >= 70 and usr_input < 80:
    print("Grade: C")
elif usr_input >= 60 and usr_input < 70:
    print("Grade: D")
elif usr_input >= 50 and usr_input < 60:
    print("Grade: E")
else:
    print("Grade: F")