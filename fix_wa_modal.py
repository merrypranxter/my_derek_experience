import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Add import
if 'import ChatModal' not in content:
    content = content.replace('import TTSButton from "../components/TTSButton";', 'import TTSButton from "../components/TTSButton";\nimport ChatModal from "../components/ChatModal";')

# Add state
if 'const [activeChatId' not in content:
    content = content.replace('const [lightbox, setLightbox] = useState<any | null>(null);', 'const [lightbox, setLightbox] = useState<any | null>(null);\n  const [activeChatId, setActiveChatId] = useState<string | null>(null);')

# Add modal to return
if '<ChatModal' not in content:
    # Find the end of the return statement
    content = content.replace('      </div>\n    </div>\n  );\n}\n', '      </div>\n\n      <ChatModal chatId={activeChatId} onClose={() => setActiveChatId(null)} />\n    </div>\n  );\n}\n')

# Modify the linkHref logic
target = """                    let linkHref = reg && reg.url ? reg.url : null;
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
                           rel="noopener noreferrer" 
                           onPointerEnter={() => handleEidEnter(dataEid)}
                          onPointerLeave={() => handleEidLeave(dataEid)}
                        >
                          <span dangerouslySetInnerHTML={{ __html: innerHTML }} />
                        </a>
                      );
                    }"""

replacement = """                    let linkHref = reg && reg.url ? reg.url : null;
                    const isWA = sc === 'WA';
                    
                    const innerHTML = `${id}${d ? ` <span class="d">· ${d}</span>` : ''}${(linkHref || isWA) ? ' <span class="ext">↗</span>' : ''}`;
                    
                    if (isWA) {
                      return (
                        <button
                          key={idx}
                          type="button"
                          className={cls}
                          data-eid={dataEid}
                          onClick={() => setActiveChatId(id)}
                          onPointerEnter={() => handleEidEnter(dataEid)}
                          onPointerLeave={() => handleEidLeave(dataEid)}
                        >
                          <span dangerouslySetInnerHTML={{ __html: innerHTML }} />
                        </button>
                      );
                    } else if (linkHref) {
                      return (
                        <a 
                           key={idx}
                           className={cls}
                           data-eid={dataEid}
                           href={linkHref}
                           target="_blank"
                           rel="noopener noreferrer" 
                           onPointerEnter={() => handleEidEnter(dataEid)}
                          onPointerLeave={() => handleEidLeave(dataEid)}
                        >
                          <span dangerouslySetInnerHTML={{ __html: innerHTML }} />
                        </a>
                      );
                    }"""

content = content.replace(target, replacement)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
