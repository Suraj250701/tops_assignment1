# Write a Python program that manipulates and prints strings using various string methods.

def string_manipulation(input_string):
    # Convert the string to uppercase
    upper_string = input_string.upper()
    
    # Convert the string to lowercase
    lower_string = input_string.lower()
    
    # Capitalize the first letter of the string
    capitalized_string = input_string.capitalize()
    
    # Find the length of the string
    string_length = len(input_string)
    
    # Replace 'a' with 'o' in the string
    replaced_string = input_string.replace('s', 'S')
    
    return {
        "upper": upper_string,
        "lower": lower_string,
        "capitalized": capitalized_string,
        "length": string_length,
        "replaced": replaced_string
    }

# Example usage
input_string = input("Enter a string for manipulation: ")
manipulated_results = string_manipulation(input_string)
print("Uppercase:", manipulated_results["upper"])
print("Lowercase:", manipulated_results["lower"])
print("Capitalized:", manipulated_results["capitalized"])
print("Length of string:", manipulated_results["length"])
print("Replaced 's' with 'S':", manipulated_results["replaced"])
