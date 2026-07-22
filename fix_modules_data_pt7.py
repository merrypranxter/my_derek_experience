import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Just use regex to fix it
content = re.sub(r'(next:\[.*?\])\s*\'12\':\s*\{', r'\1\n  },\n  \'12\': {', content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed via regex")
