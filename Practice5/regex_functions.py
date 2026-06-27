import re

text = "Python is easy. Python is powerful."

# search
result = re.search("Python", text)
print("search:", result.group())

# findall
result = re.findall("Python", text)
print("findall:", result)

# split
result = re.split(r"\s", text)
print("split:", result)

# sub
result = re.sub("Python", "Java", text)
print("sub:", result)

# match
result = re.match("Python", text)
print("match:", result.group())
