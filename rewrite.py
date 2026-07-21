import re

with open('backup_index.css', 'r') as f:
    content = f.read()

# Replace .docket correctly
content = re.sub(r'\.docket\s*\{[^}]+\}', """.docket{
  position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  z-index:2;text-align:center;max-width:62%;
  pointer-events:none;
}
.docket .subject,.docket a{pointer-events:auto;}""", content)

# Replace .orbit correctly
content = re.sub(r'\.orbit\s*\{[^}]+\}', """.orbit{
  position:relative;
  width:min(96vw, 1200px);
  height:min(88vh, 820px);
  list-style:none;margin:0 auto;padding:0;
}""", content)

# Find the exact media query block and replace it
# We'll just find `@media (max-width: 719px)` up to the next `@media`
# Actually, the original one was:
mq_pattern = re.compile(r'@media \(max-width: 719px\) \{.*?^\}', re.MULTILINE | re.DOTALL)
mq_replacement = """@media (max-width: 719px) {
  .orbit { position: static; width: 100%; height: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0; padding: 2rem 0; }
  .orbit__ring { display: none; }
  .docket { position: static; transform: none; max-width: 100%; margin: 0 auto 2.5rem; }
  .chip { position: static; display: flex; justify-content: center; margin-bottom: 0.6rem; }
  .chip button { transform: none; }
}"""

content = mq_pattern.sub(mq_replacement, content, count=1)

with open('src/index.css', 'w') as f:
    f.write(content)

