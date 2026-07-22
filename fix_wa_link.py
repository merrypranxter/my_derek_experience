import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

def replacer(match):
    return """                    const reg = SOURCE_REGISTRY[sc];
                    const dataEid = id.split('–')[0]; // For WA-1234–1235 types
                    
                    let linkHref = reg && reg.url ? reg.url : null;
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
                           rel={sc === 'WA' ? undefined : "noopener noreferrer"}
                          onPointerEnter={() => handleEidEnter(dataEid)}
                          onPointerLeave={() => handleEidLeave(dataEid)}
                        >
                          <span dangerouslySetInnerHTML={{ __html: innerHTML }} />
                        </a>
                      );
                    }"""

content = re.sub(r"const reg = SOURCE_REGISTRY\[sc\];[\s\S]*?if \(reg && reg.url\) \{[\s\S]*?return \([\s\S]*?<a[\s\S]*?className=\{cls\}[\s\S]*?href=\{reg.url\}[\s\S]*?>[\s\S]*?</a>[\s\S]*?\);[\s\S]*?\}", replacer, content)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
