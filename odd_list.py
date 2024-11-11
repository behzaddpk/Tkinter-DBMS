def get_odd_values(input_list):
    odd_values = [num for num in input_list if num % 2 == 0]
    return odd_values

# Example usage:
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_odd_values(input_numbers)
print("Original List:", input_numbers)
print("Odd Values:", result)
