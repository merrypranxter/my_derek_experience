with open('src/index.css', 'r') as f:
    content = f.read()

font_face = "@font-face{ font-family:'Junegull'; src:url('https://raw.githubusercontent.com/merrypranxter/fuckyou_derek/main/assets/fonts/junegull%20rg.woff2') format('woff2'); font-display:swap; }"

content = content.replace(font_face, "")

# Insert it after @plugin
import_str = '@plugin "@tailwindcss/typography";\n'
if import_str in content:
    content = content.replace(import_str, import_str + font_face + "\n")

with open('src/index.css', 'w') as f:
    f.write(content)

