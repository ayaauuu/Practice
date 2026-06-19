class Animal:

    def speak(self):
        print("Animal sound")

class Cat(Animal):

    def speak(self):
        print("Meow")

class Dog(Animal):

    def speak(self):
        print("Woof")

cat = Cat()
dog = Dog()

cat.speak()
dog.speak()
