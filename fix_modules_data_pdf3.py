import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Make module 11's PDF work by removing the pdf property and just putting a link in the note or analysis
target = """        media: [{type: "pdf", url: "/assets/derek_original_chat.txt.pdf"}] }"""
replacement = """        note: "The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia. <a href='/derek_original_chat.txt.pdf' target='_blank' style='color:var(--atm-cyan); text-decoration:underline;'>[DOWNLOAD PDF AUDIT]</a>" }"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/data/modules.ts", "w") as f:
        f.write(content)
    print("Replaced media property with html link")
else:
    print("Target not found")
