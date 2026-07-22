import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Add import
if 'import ChatModal' not in content:
    content = content.replace('import TTSButton from "../components/TTSButton";', 'import TTSButton from "../components/TTSButton";\nimport ChatModal from "../components/ChatModal";')

# Add state
if 'const [activeChatId' not in content:
    content = content.replace('const [lightbox, setLightbox] = useState<any | null>(null);', 'const [lightbox, setLightbox] = useState<any | null>(null);\n  const [activeChatId, setActiveChatId] = useState<string | null>(null);')

# Modify the linkHref logic
# We will use regex to be safe
pattern = re.compile(r"let linkHref = reg && reg\.url \? reg\.url : null;\s*if \(sc === 'WA'\) \{\s*linkHref = `https://github\.com/.*?`;\s*\}\s*const innerHTML = `\$\{id\}\$\{d \? ` <span class=\"d\">· \$\{d\}</span>` : ''\}\$\{linkHref \? ' <span class=\"ext\">↗</span>' : ''\}`;\s*if \(linkHref\) \{\s*return \(\s*<a\s*key=\{idx\}\s*className=\{cls\}\s*data-eid=\{dataEid\}\s*href=\{linkHref\}\s*target=\"_blank\"\s*rel=\"noopener noreferrer\"\s*onPointerEnter=\{.*?\}\s*onPointerLeave=\{.*?\}\s*>\s*<span dangerouslySetInnerHTML=\{\{ __html: innerHTML \}\} />\s*</a>\s*\);\s*\}", re.DOTALL)

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

if pattern.search(content):
    content = pattern.sub(replacement, content)
    print("Replaced WA link logic!")
else:
    print("Could not find WA link logic to replace.")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
