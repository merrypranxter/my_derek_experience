import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """          </div>
        
        <div className="relative"><TTSButton text={parsed.objective} className="absolute -top-4 right-0" /><p className="objective">{parsed.objective}</p></div>
      </header>"""

replacement = """          </div>
        )}
        
        <div className="relative"><TTSButton text={parsed.objective} className="absolute -top-4 right-0" /><p className="objective">{parsed.objective}</p></div>
      </header>"""

content = content.replace(target, replacement)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
