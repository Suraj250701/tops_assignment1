#  Write a Python program to print the substring between index values 1 and 4.

def substring_between_indices(input_string):
    # Slicing the string between index values 1 and 4
    substring = input_string[1:4]
    return substring

print("Substring between index values 1 and 4:", substring_between_indices(input("Enter a string: ")))