import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = r'<div\s*className="mnode"\s*tabIndex=\{0\}\s*onPointerEnter=\{[^\}]+\}\s*onFocus=\{[^\}]+\}\s*onPointerLeave=\{[^\}]+\}\s*onBlur=\{[^\}]+\}\s*>\s*<div className="n">\{i \+ 1\}</div>\s*<h3>\{n\.title\}</h3>\s*<TTSButton text=\{n\.text\} className="mt-2 opacity-50 hover:opacity-100" />\s*</div>'

def replacer(match):
    # just return the desired block
    return """            <div 
               className="mnode relative" 
               tabIndex={0} 
               onPointerEnter={() => handleMechHover(n.text)}
              onFocus={() => handleMechHover(n.text)}
              onPointerLeave={handleMechLeave}
              onBlur={handleMechLeave}
            >
              <TTSButton text={n.text} className="absolute top-2 right-2 opacity-50 hover:opacity-100" />
              <div className="n">{i + 1}</div>
              <h3>{n.title}</h3>
            </div>"""

new_content, count = re.subn(target, replacer, content)

if count > 0:
    print(f"Fixed {count} mnode TTSButtons")
else:
    print("Target not found")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(new_content)
