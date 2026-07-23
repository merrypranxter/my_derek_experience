import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Remove inline media objects like `media: { type: "image", url: "https://storage.googleapis.com/..." },`
content = re.sub(r',\s*media:\s*\{\s*type:\s*"[^"]+",\s*url:\s*"https://storage.googleapis.com/astraltrash_other[^"]+"\s*\}', '', content)
content = re.sub(r'media:\s*\{\s*type:\s*"[^"]+",\s*url:\s*"https://storage.googleapis.com/astraltrash_other[^"]+"\s*\},\s*', '', content)

# Remove gallery items that I might have added from the bucket
content = re.sub(r'\s*\{\s*src:\s*"https://storage.googleapis.com/astraltrash_other[^"]+",\s*cap:\s*"[^"]*"\s*\},\s*', '\n', content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
