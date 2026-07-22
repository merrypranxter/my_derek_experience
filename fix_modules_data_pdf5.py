import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Fix duplicate note
target = """        note: "The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia. <a href='/derek_original_chat.txt.pdf' target='_blank' style='color:var(--atm-cyan); text-decoration:underline;'>[DOWNLOAD PDF AUDIT]</a>" }"""
replacement = """}"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/data/modules.ts", "w") as f:
        f.write(content)
    print("Fixed duplicate note")
else:
    print("Target not found")
