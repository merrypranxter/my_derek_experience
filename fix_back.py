with open('src/pages/VisualEvidence.tsx', 'r') as f:
    content = f.read()

content = content.replace("key={c as any}", "key={c}")
content = content.replace("setFilter(c as any)", "setFilter(c)")
content = content.replace("{c as any}", "{c}")

with open('src/pages/VisualEvidence.tsx', 'w') as f:
    f.write(content)

