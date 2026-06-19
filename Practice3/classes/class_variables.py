class Student:

    university = "KazNU"

    def __init__(self, name):
        self.name = name

s1 = Student("Aya")
s2 = Student("Ali")

print(s1.university)
print(s2.university)

print(s1.name)
print(s2.name)

Student.university = "Satbayev University"

print(s1.university)
print(s2.university)
