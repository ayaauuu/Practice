names = ["Alice", "Bob", "Charlie", "David"]
scores = [95, 88, 91, 85]

print("===== enumerate() =====")

for index, name in enumerate(names, start=1):
    print(index, name)

print("\n===== zip() =====")

for name, score in zip(names, scores):
    print(name, score)

print("\n===== Type Conversion =====")

number_string = "100"
float_string = "20.5"

print(int(number_string))
print(float(float_string))
print(str(500))
print(list("Python"))

print("\n===== Type Checking =====")

print(type(names))
print(type(scores))
print(type(number_string))
print(type(500))
print(type(20.5))
