# Write a Python program to access the first character of a string using index value.

def access_first_character():
    # Allocate a string to a variable
    user_input = input("Please enter a string: ")
    # Access the first character using index value
    first_character = user_input[0]
    # Print the first character
    print("The first character of the string is:", first_character)

# Calling the function to access the first character of a string
access_first_character()