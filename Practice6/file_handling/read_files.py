from pathlib import Path

file = Path("sample.txt")

# read()
with open(file, "r") as f:
    print("===== read() =====")
    print(f.read())

# readline()
with open(file, "r") as f:
    print("\n===== readline() =====")
    print(f.readline().strip())
    print(f.readline().strip())

# readlines()
with open(file, "r") as f:
    print("\n===== readlines() =====")
    lines = f.readlines()

for line in lines:
    print(line.strip())
