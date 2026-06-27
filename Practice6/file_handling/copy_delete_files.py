import shutil
import os
from pathlib import Path

source = Path("sample.txt")
backup = Path("sample_backup.txt")

# Copy file
shutil.copy(source, backup)
print("Backup created.")

# Delete safely
if backup.exists():
    os.remove(backup)
    print("Backup deleted.")
else:
    print("Backup not found.")
