class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

student = Student("Aya", "IT")

print(student.name)
print(student.major)
