# Write a Python program to print a string from the last character.

def string_reverse(input_string):
    # Slicing the string from the last character to the first character
    reversed_string = input_string[::-1]
    return reversed_string
 
print("String from the last character to the first character:", string_reverse(input("Enter a string: ")))
