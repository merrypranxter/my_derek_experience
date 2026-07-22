import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

content = re.sub(r'  \}\n\};', '};', content)
content = re.sub(r'\}\};$', '};', content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed extra braces")
