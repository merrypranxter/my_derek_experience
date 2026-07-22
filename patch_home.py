import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

# Add import
content = content.replace('import { Link } from "react-router-dom";', 'import { Link } from "react-router-dom";\nimport TTSButton from "../components/TTSButton";')

# Add TTSButton
target = '<div className="docket">'
replacement = '<div className="docket relative">\n          <TTSButton text={TRUTH} className="absolute -top-6 right-0" />'
content = content.replace(target, replacement)

with open("src/pages/Home.tsx", "w") as f:
    f.write(content)
print("Patched Home.tsx")
