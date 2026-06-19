# Exercise 1
# Generate squares up to N

def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input("Enter N: "))

for num in square_generator(n):
    print(num)


# Exercise 2
# Even numbers from 0 to n

n = int(input("Enter n: "))

even_numbers = (str(i) for i in range(n + 1) if i % 2 == 0)

print(",".join(even_numbers))


# Exercise 3
# Numbers divisible by 3 and 4

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)


# Exercise 4
# Squares from a to b

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)


# Exercise 5
# Countdown from n to 0

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))

for num in countdown(n):
    print(num)
