import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Replace the note field using regex since the previous target didn't include the note
target_regex = r"note:\"The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia.\","
replacement = """note:"The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia. <br><br><a href='https://storage.googleapis.com/astraltrash_other/derek/derek_original_chat.txt.pdf' target='_blank' style='color:var(--atm-cyan); text-decoration:underline;'>[DOWNLOAD PDF AUDIT]</a>","""

content = re.sub(target_regex, replacement, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("Updated note with link")
