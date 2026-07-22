import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """            <div 
               className="mnode" 
               tabIndex={0} 
               onPointerEnter={() => handleMechHover(n.text)}
              onFocus={() => handleMechHover(n.text)}
              onPointerLeave={handleMechLeave}
              onBlur={handleMechLeave}
            >
              <div className="n">{i + 1}</div>
              <h3>{n.title}</h3>
              <TTSButton text={n.text} className="mt-2 opacity-50 hover:opacity-100" />
            </div>"""

replacement = """            <div 
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

if target in content:
    content = content.replace(target, replacement)
    print("Fixed mnode TTSButton")
else:
    print("Target not found")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
