import re

with open("/app/applet/src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target1 = """          <img referrerPolicy="no-referrer" src={lightbox.src} alt={lightbox.cap ? lightbox.cap.replace(/<[^>]*>?/gm, '') : ''} />"""
replacement1 = """          <a href={lightbox.src} target="_blank" rel="noopener noreferrer" style={{ cursor: 'alias', display: 'block' }}>
            <img referrerPolicy="no-referrer" src={lightbox.src} alt={lightbox.cap ? lightbox.cap.replace(/<[^>]*>?/gm, '') : ''} />
          </a>"""

content = content.replace(target1, replacement1)

with open("/app/applet/src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
