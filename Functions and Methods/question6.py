# Write a Python program to access a string up to the fifth character using index value.

def access_up_to_fifth_character():
    # Allocate a string to a variable
    user_input = input("Please enter a string: ")
    # Access the string up to the fifth character using index value
    up_to_fifth_character = user_input[:5]
    # Print the accessed string
    print("The string up to the fifth character is:", up_to_fifth_character)

# Calling the function to access a string up to the fifth character
access_up_to_fifth_character()