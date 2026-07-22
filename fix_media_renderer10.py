import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

content = content.replace("style={{width: '100%', display: 'block'}} loading=\"lazy\" onClick={() => setLightbox({src: m.url, cap: m.alt})} style={{cursor: 'zoom-in', width: '100%', display: 'block'}} />", "loading=\"lazy\" onClick={() => setLightbox({src: m.url, cap: m.alt})} style={{cursor: 'zoom-in', width: '100%', display: 'block'}} />")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
