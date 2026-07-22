import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

content = content.replace("https://storage.googleapis.com/astraltrash_other/derek/derek_original_chat.txt.pdf", "/derek_original_chat.txt.pdf")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
