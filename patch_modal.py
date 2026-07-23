import re

with open("/app/applet/src/pages/VisualEvidence.tsx", "r") as f:
    content = f.read()

target = """                  <img src={selectedMedia.url} alt={selectedMedia.name} className="w-full h-full object-contain" referrerPolicy="no-referrer" />"""

replacement = """                  <a href={selectedMedia.url} target="_blank" rel="noopener noreferrer" className="block w-full h-full flex items-center justify-center cursor-alias">
                    <img src={selectedMedia.url} alt={selectedMedia.name} className="max-w-full max-h-full object-contain" referrerPolicy="no-referrer" />
                  </a>"""

content = content.replace(target, replacement)

with open("/app/applet/src/pages/VisualEvidence.tsx", "w") as f:
    f.write(content)
