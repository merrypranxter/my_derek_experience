with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                    let linkHref = reg && reg.url ? reg.url : null;
                    if (sc === 'WA') {
                      linkHref = `/chat?id=${dataEid}`;
                    }
                    
                    const innerHTML = `${id}${d ? ` <span class="d">· ${d}</span>` : ''}${linkHref ? ' <span class="ext">↗</span>' : ''}`;
                    
                    if (linkHref) {
                      return (
                        <a 
                           key={idx}
                           className={cls}
                           data-eid={dataEid}
                           href={linkHref}
                           target={sc === 'WA' ? undefined : "_blank"}
                           rel={sc === 'WA' ? undefined : "noopener noreferrer"}"""

replacement = """                    let linkHref = reg && reg.url ? reg.url : null;
                    if (sc === 'WA') {
                      linkHref = `https://github.com/merrypranxter/fuckyou_derek/blob/main/evidence/combined/derek_whatsapp_combined.md#${dataEid.toLowerCase()}`;
                    }
                    
                    const innerHTML = `${id}${d ? ` <span class="d">· ${d}</span>` : ''}${linkHref ? ' <span class="ext">↗</span>' : ''}`;
                    
                    if (linkHref) {
                      return (
                        <a 
                           key={idx}
                           className={cls}
                           data-eid={dataEid}
                           href={linkHref}
                           target="_blank"
                           rel="noopener noreferrer" """

if target in content:
    content = content.replace(target, replacement)
    print("Replaced successfully.")
else:
    print("Target not found.")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
