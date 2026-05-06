def list_stats(numbers):
    # Step 1: Handle empty list
    if len(numbers) == 0:
        return "Error: List is empty"

    # Step 2: Find Maximum
    maximum = numbers[0]        # assume first number is max
    for n in numbers:
        if n > maximum:         # if we find a bigger number
            maximum = n         # update maximum

    # Step 3: Find Minimum
    minimum = numbers[0]        # assume first number is min
    for n in numbers:
        if n < minimum:         # if we find a smaller number
            minimum = n         # update minimum

    # Step 4: Find Average
    total = 0
    for n in numbers:
        total = total + n       # add all numbers together
    average = total / len(numbers)  # divide by count of numbers

    return maximum, minimum, average


# Test it
numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]

maximum, minimum, average = list_stats(numbers)

print(f"List    : {numbers}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Average : {average}")