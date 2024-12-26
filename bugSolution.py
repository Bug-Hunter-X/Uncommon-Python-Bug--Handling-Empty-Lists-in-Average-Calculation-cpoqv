def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)

# Example usage with an empty list
try:
    average = calculate_average([])
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

# Example usage with a list of numbers
number_list = [10, 20, 30, 40, 50]
average = calculate_average(number_list)
print(f"The average is: {average}")
