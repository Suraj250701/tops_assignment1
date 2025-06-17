# Write a simple Python program that uses a custom iterator to iterate over a list of integers.

def custom_iterator(lst):
    for item in lst:
        yield item

usr_lst = []
lst_size = int(input("Enter the number of elements in the list: "))
for i in range(lst_size):
    element = int(input(f"Enter element {i + 1}: "))
    usr_lst.append(element)

print("Items in list : ")
for item in custom_iterator(usr_lst):
    print(item)

 

