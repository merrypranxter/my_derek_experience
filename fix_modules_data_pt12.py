import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# For 04 to 05
target = """    next:["05","MODULE 05 — THE TRIANGULATION"]
};
MODULE_DATA['05'] = {"""
replacement = """    next:["05","MODULE 05 — THE TRIANGULATION"]
  }
};
MODULE_DATA['05'] = {"""
content = content.replace(target, replacement)

# Let's check 05 to 06
target2 = """    next:["06","MODULE 06 — THE EXPLOITATION"]
};
MODULE_DATA['06'] = {"""
replacement2 = """    next:["06","MODULE 06 — THE EXPLOITATION"]
};
MODULE_DATA['06'] = {""" # wait, if 05 is assigned like MODULE_DATA['05'] = {, then it just needs }; to close the assignment.

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed 04 to 05 transition")
