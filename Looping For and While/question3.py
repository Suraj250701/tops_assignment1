# Write a Python program to find a specific string in the list using a simple for loop and if condition.

user_input = []
list_size = int(input("Enter the number of strings you want to add to the list: "))
for i in range(list_size):
    string = input(f"Enter string {i + 1}: ")
    user_input.append(string)

search_string = input("Enter the string you want to search for: ")
found = False
for string in user_input:
    if string == search_string:
        found = True
        print(f"'{search_string}' found in the list.")
        break
if not found:
    print(f"'{search_string}' not found in the list.")
    

