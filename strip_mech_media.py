import re
import json

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# We can regex replace the media inside mechanism arrays, but they're multi-line and not purely JSON.
# Instead, just remove all media tags that appear on lines starting with `{title:`. 
# In modules.ts, mechanisms are defined as `{title:"...", media: ..., text:"..."}`
content = re.sub(r'\{title:([^,]+),\s*media:\s*\{[^}]+\},\s*text:', r'{title:\1, text:', content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
