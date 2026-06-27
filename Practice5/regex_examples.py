import re

# 1. Match "a" followed by zero or more "b"
print("1.")
text = ["a", "ab", "abb", "ac", "b"]
pattern = r"ab*"

for t in text:
    if re.fullmatch(pattern, t):
        print(t)

# 2. Match "a" followed by two or three "b"

print("\n2.")
text = ["abb", "abbb", "abbbb", "ab"]

pattern = r"ab{2,3}"

for t in text:
    if re.fullmatch(pattern, t):
        print(t)

# 3. Find lowercase letters joined with underscore

print("\n3.")

text = "hello_world my_variable abc_def Test"

print(re.findall(r"[a-z]+_[a-z]+", text))

# 4. Uppercase followed by lowercase

print("\n4.")

text = "Hello WORLD Apple Python"

print(re.findall(r"[A-Z][a-z]+", text))

# 5. Starts with a ends with b

print("\n5.")

text = ["ab", "axxxb", "acccb", "abb", "abc"]

pattern = r"a.*b"

for t in text:
    if re.fullmatch(pattern, t):
        print(t)

# 6. Replace spaces commas dots with :

print("\n6.")

text = "Python, Java. C++ Language"

print(re.sub(r"[ ,\.]", ":", text))

# 7. Snake case -> Camel case

print("\n7.")

text = "hello_world_python"

parts = text.split("_")

camel = parts[0] + "".join(word.capitalize() for word in parts[1:])

print(camel)

# 8. Split at uppercase letters

print("\n8.")

text = "HelloWorldPython"

print(re.findall(r"[A-Z][a-z]*", text))

# 9. Insert spaces before capital letters

print("\n9.")

text = "HelloWorldPython"

print(re.sub(r"([A-Z])", r" \1", text).strip())

# 10. Camel case -> Snake case

print("\n10.")

text = "HelloWorldPython"

snake = re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")

print(snake)
