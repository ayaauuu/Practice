import shutil
from pathlib import Path

# Create destination folder
destination_folder = Path("Practice/Data")
destination_folder.mkdir(parents=True, exist_ok=True)

source = Path("../file_handling/sample.txt")

copy_destination = destination_folder / "sample_copy.txt"

# Copy file
shutil.copy(source, copy_destination)
print("File copied successfully.")

move_destination = destination_folder / "sample_moved.txt"

# Move file
shutil.move(copy_destination, move_destination)
print("File moved successfully.")

# Find all .txt files
print("\nSearching for .txt files:")

for file in Path("Practice").rglob("*.txt"):
    print(file)
