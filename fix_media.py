import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Replace the duplicated MediaEmbed block + first export default function ModulePage() {
# I will just find the first "const MediaEmbed" and the second "const MediaEmbed".
# The first one is at line 35. The second is at 52.

matches = list(re.finditer(r'const MediaEmbed = .*?export default function ModulePage\(\) \{', content, flags=re.DOTALL))
if len(matches) > 1:
    content = content[:matches[0].start()] + matches[1].group(0) + content[matches[1].end():]

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
