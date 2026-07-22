import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Fix the syntax error around '12': { ... }
# Find where module 11 ends and module 12 begins
target = """    prev:["module07.html","MODULE 07 — THE ERASURE"],
    next:["12","MODULE 12 — THE CUCKING"]
  
  '12': {"""
replacement = """    prev:["07","MODULE 07 — THE ERASURE"],
    next:["12","MODULE 12 — THE CUCKING"]
  },
  '12': {"""
content = content.replace(target, replacement)

# Fix next for 12
target2 = """    prev:["11","MODULE 11 — THE GHOST ANALYSIS"],
    next:["12","MODULE 12 — THE CUCKING"]
  }
};"""
replacement2 = """    prev:["11","MODULE 11 — THE GHOST ANALYSIS"],
    next:null
  }
};"""
content = content.replace(target2, replacement2)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed modules.ts")
