# Create a list of numbers from 1 to 20
numbers = [num for num in range(1, 21)]
print("Numbers 1-20:", numbers)

# Filter only even numbers from that list
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)