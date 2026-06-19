numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

greater_than_four = list(filter(lambda x: x > 4, numbers))
print(greater_than_four)

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
