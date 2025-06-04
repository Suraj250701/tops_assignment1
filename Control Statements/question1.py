# Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

def skip_item():
    # Define the list
    List1 = ['apple', 'banana', 'mango']
    
    # Iterate through the list
    for fruit in List1:
        # Skip 'banana' using continue statement
        if fruit == 'banana':
            continue
        # Print the fruit if it's not 'banana'
        print(fruit)

skip_item()