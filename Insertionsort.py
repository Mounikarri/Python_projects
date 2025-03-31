Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insertion_sort(arr):
...     for i in range(1, len(arr)):
...         key = arr[i]
...         j = i - 1
...         while j >= 0 and arr[j] > key:
...             arr[j + 1] = arr[j]
...             j -= 1
...         arr[j + 1] = key
...     return arr
... 
... # Example usage
... arr = [12, 11, 13, 5, 6]
... print(insertion_sort(arr))
