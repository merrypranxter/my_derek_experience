import re

with open('src/index.css', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if line.startswith('@media (max-width: 719px) {') and not skip:
        skip = True
        new_lines.append("""@media (max-width: 719px) {
  .orbit { width: 100%; height: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; position: static; margin: 0; }
  .orbit__ring { display: none; }
  .docket { position: static; transform: none; max-width: 100%; margin: 0 auto 2.5rem; }
  .chip { position: static; display: flex; justify-content: center; margin-bottom: 0.6rem; }
  .chip button { pointer-events: auto; transform: none; }
}
""")
        continue
    
    if skip:
        if line.startswith('}'):
            skip = False
        continue
    
    new_lines.append(line)

with open('src/index.css', 'w') as f:
    f.writelines(new_lines)
