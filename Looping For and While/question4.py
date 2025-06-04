# Print this pattern using nested for loop:
# *
# **
# ***
# ****
# *****

# Write a Python program to print a pattern using nested for loops.
user_input = int(input("Enter the number of rows for the pattern: "))
for i in range(1, user_input + 1):
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line after each row