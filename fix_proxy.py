import re

with open("src/pages/VisualEvidence.tsx", "r") as f:
    content = f.read()

# Replace the wsrv.nl proxy logic since we're using local files now
target = "src={`https://wsrv.nl/?url=${encodeURIComponent(file.url)}&w=300&q=70&output=webp`}"
replacement = "src={file.url}"

if target in content:
    content = content.replace(target, replacement)
    print("Replaced wsrv.nl proxy")
else:
    print("Target not found")
    
with open("src/pages/VisualEvidence.tsx", "w") as f:
    f.write(content)
