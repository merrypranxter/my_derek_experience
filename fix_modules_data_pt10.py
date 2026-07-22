import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Fix the transition from 11 to 12
target = """  prev:["07","MODULE 07 — THE ERASURE"],
  next:["12","MODULE 12 — THE CUCKING"]
  },
  '12': {"""
replacement = """  prev:["07","MODULE 07 — THE ERASURE"],
  next:["12","MODULE 12 — THE CUCKING"]
};
MODULE_DATA['12'] = {"""
content = content.replace(target, replacement)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed 11 to 12 transition")
