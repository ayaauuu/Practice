# Positional arguments
def student(name, age):
    print(name, age)

student("Aya", 20)

# Default argument
def country(name, country="Kazakhstan"):
    print(name, country)

country("Ali")
country("Tom", "USA")

# Keyword arguments
def person(name, age):
    print(name, age)

person(age=20, name="Nurlan")
