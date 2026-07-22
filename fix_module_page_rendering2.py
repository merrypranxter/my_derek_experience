import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                {ex.analysis && (
                  <div className="exhibit__analysis">
                    <b>[NODE_771_ANALYSIS]</b><br/>
                    <span dangerouslySetInnerHTML={{ __html: formatText(ex.analysis) }}></span>
                  </div>
                )}
              </div>
            </article>"""

replacement = """                {ex.analysis && (
                  <div className="exhibit__analysis">
                    <b>[NODE_771_ANALYSIS]</b><br/>
                    <span dangerouslySetInnerHTML={{ __html: formatText(ex.analysis) }}></span>
                  </div>
                )}
                {ex.media && ex.media.length > 0 && (
                  <div className="exhibit__media" style={{marginTop: '20px'}}>
                    {ex.media.map((m: any, mIdx: number) => (
                      <div key={mIdx} style={{marginBottom: '15px'}}>
                        {m.type === 'image' || !m.type ? (
                          <div className="img-wrap" style={{border: '1px solid var(--atm-dim)', padding: '5px', background: 'rgba(0,0,0,0.2)'}}>
                            <img src={m.url} alt={m.alt || "Exhibit Evidence"} style={{width: '100%', display: 'block'}} loading="lazy" />
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
              </div>
            </article>"""

if target in content:
    content = content.replace(target, replacement)
    print("Updated ModulePage to render media")
else:
    print("Target not found in ModulePage")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
