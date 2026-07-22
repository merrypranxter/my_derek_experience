import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Make module 11's PDF work by removing the pdf property and just putting a link in the note or analysis
target = """        note:"The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia. <br><br><a href='https://storage.googleapis.com/astraltrash_other/derek/derek_original_chat.txt.pdf' target='_blank' style='color:var(--atm-cyan); text-decoration:underline;'>[DOWNLOAD PDF AUDIT]</a>","""
replacement = """        note:"The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia.",
        media: [
            { type: "pdf", url: "https://storage.googleapis.com/astraltrash_other/derek/derek_original_chat.txt.pdf", alt: "PDF Audit" }
        ],"""

if target in content:
    content = content.replace(target, replacement)
    print("Replaced with media block")
else:
    print("Target not found")
    
with open("src/data/modules.ts", "w") as f:
    f.write(content)

