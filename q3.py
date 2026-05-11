def remove_duplicates(numbers):
    seen = []
    result = []
    for num in numbers:
        if num not in seen:
            seen.append(num)
            result.append(num)
    return result

# Example usage
nums = [1, 2, 3, 2, 4, 1, 5, 3, 6]
print("Original:", nums)
print("No duplicates:", remove_duplicates(nums))