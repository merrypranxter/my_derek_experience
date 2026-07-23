import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

bad_block = """              {ex.crossref && (
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
              )}"""

good_block = """              {ex.quote && (
                <blockquote className="exhibit__quote relative">
                  "{ex.quote}"
                </blockquote>
              )}
              {ex.note && <p className="exhibit__note" dangerouslySetInnerHTML={{ __html: ex.note }}></p>}
              {ex.analysis && <p className="exhibit__analysis" dangerouslySetInnerHTML={{ __html: `<strong>ANALYSIS:</strong> ${ex.analysis}` }}></p>}
              
              {ex.crossref && (
                 <div className="crossref-section" style={{marginTop: '20px', padding: '15px', borderLeft: '4px solid var(--atm-cyan)', background: 'rgba(53, 224, 255, 0.05)'}}>
                   <h4 style={{fontSize: '0.8rem', color: 'var(--atm-cyan)', margin: '0 0 10px 0', letterSpacing: '0.1em'}}>SEE {ex.crossref[1]}</h4>
                   <Link to={`/module/${ex.crossref[0]}`} style={{color: '#fff', textDecoration: 'none', fontWeight: 'bold'}}>Open Module {ex.crossref[0]} ↗</Link>
                 </div>
              )}"""

content = content.replace(bad_block, good_block)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
