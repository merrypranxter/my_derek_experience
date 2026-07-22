import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Let's fix the PDF structure to be a single exhibit with the PDF data, and add a link to the PDF
target = """        pdf:"/assets/derek_original_chat.txt.pdf" }"""
replacement = """        media: [{type: "pdf", url: "/assets/derek_original_chat.txt.pdf"}] }"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/data/modules.ts", "w") as f:
        f.write(content)
    print("Replaced pdf property")
else:
    print("Target not found")
