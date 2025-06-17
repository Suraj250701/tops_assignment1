# Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce as rd

def product(x, y):
    return x * y

def product_of_numbers(numbers):
    return rd(product, numbers)

usr_lst = []
lst_size = int(input("Enter the number of elements in the list: "))
for i in range(lst_size):
    element = int(input(f"Enter element {i + 1}: "))
    usr_lst.append(element)
print("Product of numbers:", product_of_numbers(usr_lst))