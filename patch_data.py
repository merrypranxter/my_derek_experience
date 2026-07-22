import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

target = """        name:"The “Dedicated Duet Partner” Contract","""

replacement = """        name:"The “Dedicated Duet Partner” Contract",
        image:"https://storage.googleapis.com/astraltrash_other/derek/DUET_PARTNER_ORIGINAL.PNG","""

content = content.replace(target, replacement)

with open("src/data/modules.ts", "w") as f:
    f.write(content)

print("Patched modules.ts")
