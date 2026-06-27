from pathlib import Path

file = Path("sample.txt")

# File mode: w
with open(file, "w") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Charlie\n")

print("File created using mode 'w'.")

# File mode: a
with open(file, "a") as f:
    f.write("David\n")
    f.write("Emma\n")

print("New lines appended.")

# File mode: x
new_file = Path("new_file.txt")

if not new_file.exists():
    with open(new_file, "x") as f:
        f.write("This file was created using mode x.")
    print("new_file.txt created.")
else:
    print("new_file.txt already exists.")
