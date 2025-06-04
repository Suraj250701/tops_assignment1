#  Write a Python program to stop the loop once 'banana' is found using the break statement.

def stop_on_banana():
    # Define the list
    List1 = ['apple', 'banana', 'mango']
    
    for fruit in List1:
        # Stop the loop if 'banana' is found using break statement
        if fruit == 'banana':
            print("Found banana, stopping the loop.")
            break
        print(fruit)

stop_on_banana()