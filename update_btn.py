import re

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

content = content.replace('className="flex items-center gap-[.55em] font-subject text-[.68rem] tracking-[.24em] pointer-events-auto"', '')
content = content.replace('<b className="font-normal tracking-[.06em] text-red-500">', '<b>')

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)

