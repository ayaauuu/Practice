students = [
    ("Ali", 20),
    ("Aya", 18),
    ("Tom", 25)
]

sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)

words = ["banana", "kiwi", "watermelon", "apple"]

sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
