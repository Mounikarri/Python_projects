Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def quick_sort(arr):
...     if len(arr) <= 1:
...         return arr
...     pivot = arr[len(arr) // 2]
...     left = [x for x in arr if x < pivot]
...     middle = [x for x in arr if x == pivot]
...     right = [x for x in arr if x > pivot]
...     return quick_sort(left) + middle + quick_sort(right)
... 
... # Example usage
... arr = [3, 6, 8, 10, 1, 2, 1]
... print(quick_sort(arr))
