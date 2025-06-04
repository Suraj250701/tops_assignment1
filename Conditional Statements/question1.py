# Write a Python program to find greater and less than a number using if_else

usr_input = int(input("Enter a number1: "))
usr_input2 = int(input("Enter a number2: "))
if usr_input < usr_input2:
    print(f"{usr_input} is less than {usr_input2}")
else:
    print(f"{usr_input} is greater than or equal to {usr_input2}")