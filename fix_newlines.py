import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Replace the specific double quotes with backticks
target = """{ title: "THE NUMBERS", text: "How he made such a cuck of me"""
replacement = """{ title: "THE NUMBERS", text: `How he made such a cuck of me"""
content = content.replace(target, replacement)

target2 = """He made a big deal out of that duet partnership." },"""
replacement2 = """He made a big deal out of that duet partnership.` },"""
content = content.replace(target2, replacement2)

# Also fix module 01
target3 = """{ title: "THE SPOT ON HIS PROFILE", text: "And it wasn't just"""
replacement3 = """{ title: "THE SPOT ON HIS PROFILE", text: `And it wasn't just"""
content = content.replace(target3, replacement3)

target4 = """Okay, well we'll go into Jay in another module." },"""
replacement4 = """Okay, well we'll go into Jay in another module.` },"""
content = content.replace(target4, replacement4)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed newlines in strings")
