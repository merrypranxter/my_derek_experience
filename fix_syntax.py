import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                    if (linkHref) {
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
                    })}"""

replacement = """                    if (linkHref) {
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
                    }
                    return <span key={idx} className={cls} dangerouslySetInnerHTML={{ __html: innerHTML }} />;
                  })}"""

if target in content:
    content = content.replace(target, replacement)
    print("Fixed syntax")
else:
    print("Target not found")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
