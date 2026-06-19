numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

plus_ten = list(map(lambda x: x + 10, numbers))
print(plus_ten)
