with open('src/index.css', 'r') as f:
    lines = f.readlines()

replacement = """@media (max-width: 719px) {
  .orbit { position: static; width: 100%; height: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 2rem 0; }
  .orbit__ring { display: none; }
  .docket { position: static; transform: none; max-width: 100%; margin: 0 auto 2.5rem; pointer-events: auto; }
  .docket .subject, .docket a { pointer-events: auto; }
  .chip { position: static; display: flex; justify-content: center; width: 100%; margin-bottom: 0.6rem; }
  .chip button { transform: none; pointer-events: auto; }
}
"""

# Replace lines 219 to 237 (0-indexed 218 to 236)
new_lines = lines[:218] + [replacement] + lines[237:]

with open('src/index.css', 'w') as f:
    f.writelines(new_lines)
