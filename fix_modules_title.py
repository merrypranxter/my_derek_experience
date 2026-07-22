import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

content = content.replace('title:"THE FORENSICS"', 'title:"FORENSICS"')
content = content.replace('MODULE 11 — THE FORENSICS', 'MODULE 11 — FORENSICS')

with open("src/data/modules.ts", "w") as f:
    f.write(content)
