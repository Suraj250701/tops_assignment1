# Write a Python program to print every alternate character from the string starting from index 1.

def alternate_characters(input_string):
    # Slicing the string to get every alternate character starting from index 1
    alternate_string = input_string[1::2]
    return alternate_string

print("Every alternate character from the string starting from index 1:", alternate_characters(input("Enter a string: ")))