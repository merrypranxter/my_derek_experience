import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Fix syntax error in Module 12 where comma is missing
target4 = """        ] }
      { num:"12.5", status:"SHAME_REASSIGNED","""
replacement4 = """        ] },
      { num:"12.6", status:"SHAME_REASSIGNED","""

if target4 in content:
    content = content.replace(target4, replacement4)
    print("Fixed syntax error")
else:
    print("Target 4 not found")

with open("src/data/modules.ts", "w") as f:
    f.write(content)

