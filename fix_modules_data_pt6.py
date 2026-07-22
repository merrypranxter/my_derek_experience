import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

target = """  prev:["07","MODULE 07 — THE ERASURE"],
  next:["12","MODULE 12 — THE CUCKING"]
  '12': {"""
replacement = """  prev:["07","MODULE 07 — THE ERASURE"],
  next:["12","MODULE 12 — THE CUCKING"]
  },
  '12': {"""
content = content.replace(target, replacement)

# Try with module07.html just in case
target2 = """  prev:["module07.html","MODULE 07 — THE ERASURE"],
  next:["12","MODULE 12 — THE CUCKING"]
  '12': {"""
replacement2 = """  prev:["07","MODULE 07 — THE ERASURE"],
  next:["12","MODULE 12 — THE CUCKING"]
  },
  '12': {"""
content = content.replace(target2, replacement2)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed modules.ts again")
