import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Fix epigraphs
content = re.sub(
    r'(</cite>\s*</blockquote>\s*\)\)}\s*</div>)',
    r'\1\n        )}',
    content
)

# Fix labels? No, that's </ul>.

# Let's fix them manually based on the errors.
