import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Replace \' with '
content = content.replace("\\'", "'")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed backslashes")
