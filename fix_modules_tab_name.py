import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

content = content.replace('title:"THE GHOST ANALYSIS"', 'title:"THE FORENSICS"')
content = content.replace('MODULE 11 — THE GHOST ANALYSIS', 'MODULE 11 — THE FORENSICS')

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("Updated tab name")
