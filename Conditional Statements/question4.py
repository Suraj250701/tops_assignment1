# Write a Python program to check if a person is eligible to donate blood using a nested if.

usr_input = int(input("Enter your age: "))
if usr_input < 18:
    print("You are not eligible to donate blood because you are under 18 years old.")
elif usr_input > 65:
    print("You are not eligible to donate blood because you are over 65 years old.")
else:
    weight = int(input("Enter your weight in kg: "))
    if weight < 50:
        print("You are not eligible to donate blood because you weight less than 50 kg.")
    else:
        print("You are eligible to donate blood.")
