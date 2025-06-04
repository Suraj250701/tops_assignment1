# Write a Python program to demonstrate string slicing.

def demonstrate_string_slicing(input_string):
    # Slicing the string to get different parts
    first_five_characters = input_string[:5]  # First five characters
    last_five_characters = input_string[-5:]   # Last five characters
    every_second_character = input_string[::2]  # Every second character
    substring_1_to_4 = input_string[1:4]        # Substring from index 1 to 4
    reverse_string = input_string[::-1]          # Reverse the string

    return (first_five_characters, last_five_characters, every_second_character, substring_1_to_4, reverse_string)

# Example usage
input_string = input("Enter a string to demonstrate slicing: ")
sliced_results = demonstrate_string_slicing(input_string)
print("First five characters:", sliced_results[0])
print("Last five characters:", sliced_results[1])   
print("Every second character:", sliced_results[2])
print("Substring from index 1 to 4:", sliced_results[3])
print("Reversed string:", sliced_results[4])
