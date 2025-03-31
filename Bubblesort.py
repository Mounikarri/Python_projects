Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bubble_sort(arr):
...     n = len(arr)
...     for i in range(n):
...         for j in range(0, n-i-1):
...             if arr[j] > arr[j + 1]:
...                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
...     return arr
... 
... # Example usage
... arr = [64, 34, 25, 12, 22, 11, 90]
... print(bubble_sort(arr))
