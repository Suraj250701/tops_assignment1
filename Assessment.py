# Create a mini-project where students combine conditional statements, loops, and functions to create a basic Python application, such as a simple calculator or a grade management system.

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is {result}")
                else:
                    print("Error! Division by zero.")
            break
        else:
            print("Invalid input, please try again.")

calculator()