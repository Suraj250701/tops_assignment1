# Write a Python program to find the length of each string in List1.

usr_input = []
lst_size = int(input("Enter the number of strings you want to add to the list: "))
for i in range(lst_size):
    string = input(f"Enter string {i + 1}: ")
    usr_input.append(string)

print("Length of each string in the list:")
for string in usr_input:
    print(f"Length of '{string}': {len(string)}")
    