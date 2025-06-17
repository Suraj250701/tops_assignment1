# Write a generator function that generates the first 10 even numbers.

def generate_even_numbers(n):
    for i in range(n):
        yield i * 2

for even_number in generate_even_numbers(10):
    print(even_number)