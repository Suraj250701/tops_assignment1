# Write a Python program that filters out even numbers using the filter() function.

# def isEven(x):
#     return x % 2 == 0

def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

usr_lst = []
lst_size = int(input("Enter the number of elements in the list: ")) 
for i in range(lst_size):
    element = int(input(f"Enter element {i + 1}: "))
    usr_lst.append(element)
print("Even numbers:", filter_even_numbers(usr_lst))