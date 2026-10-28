name = "albert einstein"
quote = "A person who never made a mistake never tried anything new."
message = f'{name.title()} once said, "{quote}"'
print(message)

# White space stripping.
name_space = "  albert einstein    "
print(name_space.lstrip())
print(name_space.rstrip())
print(name_space.strip())

# Remove suffix
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
