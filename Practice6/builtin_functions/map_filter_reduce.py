from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:")
print(numbers)

# map()
squares = list(map(lambda x: x * x, numbers))
print("\nSquares:")
print(squares)

# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nEven numbers:")
print(even_numbers)

# reduce()
total = reduce(lambda x, y: x + y, numbers)
print("\nReduce (sum):")
print(total)

print("\nBuilt-in Functions")

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sorted Descending:", sorted(numbers, reverse=True))
