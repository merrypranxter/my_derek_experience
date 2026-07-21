with open('src/pages/VisualEvidence.tsx', 'r') as f:
    content = f.read()

content = content.replace("key={cat as string}", "key={c}")
content = content.replace("setFilter(cat as string)", "setFilter(c)")
content = content.replace("{cat as string}", "{c}")
content = content.replace("filter === cat", "filter === c")

with open('src/pages/VisualEvidence.tsx', 'w') as f:
    f.write(content)

