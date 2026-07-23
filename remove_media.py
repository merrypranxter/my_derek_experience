import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# I will just remove the `media: { ... }, ` part from all mechanism and addendum text where it was wrongly added,
# or rather, I'll remove it if it has face.gif, face2.gif, ugh1.jpg, ugh2.jpg, acknowledgemeho.jpg, leaving2.mp4, leaving6.mp4, leaving5.mp4

wrong_urls = [
    "https://storage.googleapis.com/astraltrash_other/derek/ugh1.jpg",
    "https://storage.googleapis.com/astraltrash_other/derek/ugh2.jpg",
    "https://storage.googleapis.com/astraltrash_other/derek/face.gif",
    "https://storage.googleapis.com/astraltrash_other/derek/face2.gif",
    "https://storage.googleapis.com/astraltrash_other/derek/acknowledgemeho.jpg",
    "https://storage.googleapis.com/astraltrash_other/derek/leaving2.mp4",
    "https://storage.googleapis.com/astraltrash_other/derek/leaving5.mp4",
    "https://storage.googleapis.com/astraltrash_other/derek/leaving6.mp4",
]

for url in wrong_urls:
    content = re.sub(r'media:\s*\{\s*type:\s*"[^"]+",\s*url:\s*"' + re.escape(url) + r'"\s*\},\s*', '', content)
    content = re.sub(r',\s*media:\s*\{\s*type:\s*"[^"]+",\s*url:\s*"' + re.escape(url) + r'"\s*\}', '', content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
