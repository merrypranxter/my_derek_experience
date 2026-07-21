with open('src/index.css', 'r') as f:
    content = f.read()

content = content.replace("@font-face{ font-family:'Junegull'; src:url('https://raw.githubusercontent.com/merrypranxter/fuckyou_derek/main/assets/fonts/junegull%20rg.woff2') format('woff2'); font-display:swap; }", "")

new_content = "@font-face{ font-family:'Junegull'; src:url('https://raw.githubusercontent.com/merrypranxter/fuckyou_derek/main/assets/fonts/junegull%20rg.woff2') format('woff2'); font-display:swap; }\n" + content

with open('src/index.css', 'w') as f:
    f.write(new_content)
