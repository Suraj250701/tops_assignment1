# Write a Python program to access the string from the second position onwards using slicing.

def access_string_from_second_position(input_string):
    # Slicing the string from the second position onwards
    sliced_string = input_string[1:]
    return sliced_string

user_input = input("Enter a string: ")
print("String from the second position onwards:", access_string_from_second_position(user_input))
