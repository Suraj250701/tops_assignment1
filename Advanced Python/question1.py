# Write a Python program to apply the map() function to square a list of numbers.


def square(x):
    return x * x

def square_numbers(numbers):
    return list(map(square, numbers))

usr_lst = []
lst_size = int(input("Enter the number of elements in the list: "))
for i in range(lst_size):
    element = int(input(f"Enter element {i + 1}: "))
    usr_lst.append(element)
print("Squared numbers:", square_numbers(usr_lst))


