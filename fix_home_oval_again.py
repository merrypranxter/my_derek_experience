import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

target = """      const a = Math.min(W * 0.45, W / 2 - 100);
      const b = Math.min(H * 0.42, H / 2 - 80);"""

replacement = """      // Oval that fits on the page with nice breathing room around the title
      const a = Math.min(W * 0.44, W / 2 - 110);
      const b = Math.min(H * 0.40, H / 2 - 60);"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/pages/Home.tsx", "w") as f:
        f.write(content)
    print("Replaced oval dimensions successfully")
else:
    print("Target not found. Doing regex fallback...")
    content = re.sub(r'const a = Math\.min\(W \* [0-9.]+, W / 2 - [0-9.]+\);.*const b = Math\.min\(H \* [0-9.]+, H / 2 - [0-9.]+\);', r'const a = Math.min(W * 0.44, W / 2 - 110);\n      const b = Math.min(H * 0.40, H / 2 - 60);', content, flags=re.DOTALL)
    with open("src/pages/Home.tsx", "w") as f:
        f.write(content)
    print("Replaced with regex.")

