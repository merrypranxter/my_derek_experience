import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

# Make sure the title reflects the 13 modules if we added one (Module 12)
target = "an archive in twelve modules. the record does not change."
replacement = "an archive in thirteen modules. the record does not change."

if target in content:
    content = content.replace(target, replacement)
    print("Updated title to thirteen modules")
else:
    print("Target not found")
    
with open("src/pages/Home.tsx", "w") as f:
    f.write(content)
