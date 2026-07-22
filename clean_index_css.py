import re

with open('src/index.css', 'r') as f:
    content = f.read()

# We only want to keep the tailwind imports at the top, and remove all the custom CSS that is now in module.css
tailwind_imports = """@import "tailwindcss";

@theme {
  --color-atm-bg: #05030f;
  --color-atm-ink: #e8e4d8;
  --color-atm-dim: #6f6a80;
  --color-atm-stamp: #ff3b30;
  --color-atm-cyan: #35e0ff;
  --color-atm-magenta: #ff2ea6;
  --font-subject: 'Junegull', 'Arial Black', sans-serif;
  --font-archive: 'Special Elite', 'Courier New', monospace;
  --font-data: 'Space Mono', 'Courier New', monospace;
}
"""

with open('src/index.css', 'w') as f:
    f.write(tailwind_imports)

print("Cleaned index.css")
