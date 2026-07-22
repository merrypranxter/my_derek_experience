import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """            {parsed.epigraphs.map((q: any, i: number) => (
              <blockquote key={i} className={`epigraph ${q.who === 'Derek' ? 'him' : 'her'}`}>
                <p>{q.text}</p>
                <cite>— {q.who.toUpperCase()} · {q.src}</cite>
              </blockquote>
            ))}"""

replacement = """            {parsed.epigraphs.map((q: any, i: number) => (
              <blockquote key={i} className={`epigraph ${q.who === 'Derek' ? 'him' : 'her'}`}>
                <p>{q.text}</p>
                <cite>— {q.who ? `${q.who.toUpperCase()} · ` : ''}{q.src || q.source}</cite>
              </blockquote>
            ))}"""

if target in content:
    content = content.replace(target, replacement)
    print("Replaced epigraphs toUpperCase bug")
else:
    print("Target not found")
    
with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
