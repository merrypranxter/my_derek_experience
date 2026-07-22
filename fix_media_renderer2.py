import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                {exhibit.media.map((m, mIdx) => (
                  <div key={mIdx} className="exhibit-media">
                    <img src={m.url} alt={m.alt || "Exhibit media"} className="exhibit-image" />
                  </div>
                ))}"""

replacement = """                {exhibit.media.map((m, mIdx) => (
                  <div key={mIdx} className="exhibit-media">
                    {m.type === 'image' || !m.type ? (
                      <img src={m.url} alt={m.alt || "Exhibit media"} className="exhibit-image" />
                    ) : m.type === 'pdf' ? (
                      <div className="pdf-container" style={{background: 'var(--atm-bg)', padding: '15px', border: '1px solid var(--atm-cyan)', borderRadius: '4px'}}>
                        <a href={m.url} target="_blank" rel="noreferrer" style={{color: 'var(--atm-cyan)', textDecoration: 'underline', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px'}}>
                          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                          VIEW / DOWNLOAD PDF DOCUMENT: {m.alt || "Document"}
                        </a>
                      </div>
                    ) : null}
                  </div>
                ))}"""

if target in content:
    content = content.replace(target, replacement)
    print("Updated renderer 2")
else:
    print("Target 2 not found")
    
with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
