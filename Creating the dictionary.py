def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index of the target
    return -1  # Return -1 if the target is not found

# Example usage
numbers = [3, 5, 2, 9, 6]
target = 9
result = linear_search(numbers, target)
print(f'Linear Search: Target {target} found at index {result}.')
