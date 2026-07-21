with open('src/index.css', 'r') as f:
    content = f.read()

font_face = "@font-face{ font-family:'Junegull'; src:url('https://raw.githubusercontent.com/merrypranxter/fuckyou_derek/main/assets/fonts/junegull%20rg.woff2') format('woff2'); font-display:swap; }\n"
content = content.replace(font_face, "")

theme_end = content.find("}\n\nbody {")
if theme_end == -1:
    theme_end = content.find("}\nbody {")
    
if theme_end != -1:
    content = content[:theme_end+1] + "\n\n" + font_face + content[theme_end+1:]

with open('src/index.css', 'w') as f:
    f.write(content)
