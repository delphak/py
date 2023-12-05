def recursive_sum(data):
     # Base case: if data is a number, return it
     if isinstance(data, int):
         return data
     # Recursive case: sum the elements of a list (numbers or sublists)
     else:
         return sum(recursive_sum(item) for item in data)

# Usage example
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
result = recursive_sum(nested_list)
print(f"Sum of list elements: {result}")
