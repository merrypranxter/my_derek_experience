import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

target = "an archive in twelve modules. the record does not change."
replacement = "an archive in thirteen modules. the record does not change."

if target in content:
    content = content.replace(target, replacement)
    print("Updated title")
else:
    print("Target not found - maybe already 13?")
    
with open("src/pages/Home.tsx", "w") as f:
    f.write(content)
