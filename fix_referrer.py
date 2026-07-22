with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

content = content.replace('loading="lazy" />', 'loading="lazy" referrerPolicy="no-referrer" />')

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)

with open("src/pages/VisualEvidence.tsx", "r") as f:
    content = f.read()

content = content.replace('loading="lazy"', 'loading="lazy" referrerPolicy="no-referrer"')
content = content.replace('className="w-full h-full object-contain" />', 'className="w-full h-full object-contain" referrerPolicy="no-referrer" />')

with open("src/pages/VisualEvidence.tsx", "w") as f:
    f.write(content)
