import os
from pathlib import Path

# mkdir()
os.mkdir("ExampleFolder")

# makedirs()
os.makedirs("Practice/Data/Images", exist_ok=True)

print("Current directory:")
print(os.getcwd())

print("\nFiles and folders:")
for item in os.listdir():
    print(item)

# chdir()
os.chdir("Practice")

print("\nChanged directory:")
print(os.getcwd())

os.chdir("..")

# rmdir()
os.mkdir("DeleteMe")
os.rmdir("DeleteMe")

print("\nDeleteMe folder removed.")
