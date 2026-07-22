import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                    return <span key={idx} className={cls} dangerouslySetInnerHTML={{ __html: innerHTML }} />;
                  })}
      </div>"""

replacement = """                    return <span key={idx} className={cls} dangerouslySetInnerHTML={{ __html: innerHTML }} />;
                  })}
                </div>
              )}
              
              {ex.crossref && (
                 <>
                   <p className="exhibit__desc" dangerouslySetInnerHTML={{ __html: ex.desc }}></p>
                   <div className="crossref-section">
                     <h4>See Module {ex.crossref.id}</h4>
                     <Link to={`/module/${ex.crossref.id}`}>Open Module {ex.crossref.id} ↗</Link>
                   </div>
                 </>
              )}
              
              {!ex.crossref && (
                <p className="exhibit__desc" dangerouslySetInnerHTML={{ __html: ex.desc }}></p>
              )}

              {ex.media && ex.media.length > 0 && (
                <div className="exhibit__media" style={{marginTop: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'flex-start'}}>
                  {ex.media.map((m: any, mIdx: number) => (
                    <div key={mIdx} style={{marginBottom: '15px', flex: '1 1 300px'}}>
                      {m.type === 'image' || !m.type ? (
                        <div className="img-wrap" style={{border: '1px solid var(--atm-dim)', padding: '5px', background: 'rgba(0,0,0,0.2)'}}>
                          <img src={m.url} alt={m.alt || "Exhibit Evidence"} loading="lazy" onClick={() => setLightbox({src: m.url, cap: m.alt})} style={{cursor: 'zoom-in', width: '100%', display: 'block'}} />
                        </div>
                      ) : m.type === 'pdf' ? (
                        <a href={m.url} target="_blank" rel="noreferrer" style={{display: 'inline-block', padding: '10px 15px', border: '1px solid var(--atm-cyan)', background: 'var(--atm-bg)', color: 'var(--atm-cyan)', fontWeight: 'bold', textDecoration: 'none'}}>
                          📄 VIEW PDF DOCUMENT: {m.alt || "Document"}
                        </a>
                      ) : null}
                    </div>
                  ))}
                </div>
              )}
            </article>
          );
        })}
      </div>"""

if target in content:
    content = content.replace(target, replacement)
    print("Fixed end chunk")
else:
    print("Target not found")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
