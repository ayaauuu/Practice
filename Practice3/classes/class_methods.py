class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

student1 = Student("Aya")
student2 = Student("Ali")

student1.introduce()
student2.introduce()
