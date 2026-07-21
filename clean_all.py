import re

with open('src/index.css', 'r') as f:
    content = f.read()

content = re.sub(r'\.docket\s*\{[^}]+\}', '', content)
content = re.sub(r'\.docket \.subject,\s*\.docket a\s*\{[^}]+\}', '', content)
content = re.sub(r'\.orbit\s*\{[^}]+\}', '', content)
content = re.sub(r'\.orbit__ring\s*\{[^}]+\}', '', content)
content = re.sub(r'\.orbit__ring circle,\s*\.orbit__ring ellipse\s*\{[^}]+\}', '', content)
content = re.sub(r'\.orbit__ring circle\s*\{[^}]+\}', '', content)
content = re.sub(r'\.chip\s*\{[^}]+\}', '', content)
content = re.sub(r'\.chip button\s*\{[^}]+\}', '', content)
content = re.sub(r'\.chip button b\s*\{[^}]+\}', '', content)
content = re.sub(r'\.chip button:hover,\s*\.chip button:focus\s*\{[^}]+\}', '', content)
content = re.sub(r'\.chip\.pulse button\s*\{[^}]+\}', '', content)
content = re.sub(r'@media \(max-width: 719px\)\s*\{\s*\}', '', content)

with open('src/index.css', 'w') as f:
    f.write(content)
