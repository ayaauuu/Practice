# *args example
def sum_numbers(*args):
    print(sum(args))

sum_numbers(1, 2, 3, 4, 5)

# **kwargs example
def information(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

information(name="Aya", age=19)

# Combined example
def show(*args, **kwargs):
    print(args)
    print(kwargs)

show(10, 20, city="Almaty")
