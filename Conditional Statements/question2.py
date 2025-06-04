# Write a Python program to check if a number is prime using if_else.

usr_input = int(input("Enter a number to check if is prime or not : "))
for i in range(2, usr_input):
    if usr_input % i == 0:
        print(f"{usr_input} is not a prime number.")
        break
else:
    print(f"{usr_input} is a prime number.")
    