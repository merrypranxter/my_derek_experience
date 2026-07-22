import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

content = content.replace('{ id: "11", title: "THE GHOST ANALYSIS"', '{ id: "11", title: "THE FORENSICS"')

with open("src/pages/Home.tsx", "w") as f:
    f.write(content)
print("Updated tab name in Home.tsx")
