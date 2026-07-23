import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Remove remaining gallery items
content = re.sub(r'\{[^{}]*src\s*:\s*"https://storage.googleapis.com/astraltrash_other[^"]+"[^{}]*\}', '', content)

# Remove `image: "..."`
content = re.sub(r',\s*image:\s*"https://storage.googleapis.com/astraltrash_other[^"]+"', '', content)
content = re.sub(r'image:\s*"https://storage.googleapis.com/astraltrash_other[^"]+",\s*', '', content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
