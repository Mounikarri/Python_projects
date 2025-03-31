def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage
sorted_numbers = [2, 3, 5, 6, 9]
target = 6
result = binary_search(sorted_numbers, target)
print(f'Binary Search: Target {target} found at index {result}.')
