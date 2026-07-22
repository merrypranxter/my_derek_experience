import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

content = content.replace("\\'12\\'", "'12'")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed backslashes")
