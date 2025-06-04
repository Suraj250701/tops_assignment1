# This program demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines.

# Write a Python program to count the number of digits and letters in a string.
digit = 0
string = 0
# Get user input
usr_str = input("Please enter the string : ")

# Count digits and letters
for i in usr_str:
    # Check if character is a digit
    if i.isdigit() :
        digit += 1
    # Check if character is a letter
    else :
        string += 1
# Display the counts
print(f"Digits = {digit} and Letters = {string}")
