import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                <div className="exhibit__media" style={{marginTop: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'flex-start'}}>
                  {ex.media.map((m: any, mIdx: number) => (
                    <div key={mIdx} style={{marginBottom: '15px'}}>
                      {m.type === 'image' || !m.type ? (
                        <div className="img-wrap" style={{border: '1px solid var(--atm-dim)', padding: '5px', background: 'rgba(0,0,0,0.2)'}}>
                          <img src={m.url} alt={m.alt || "Exhibit Evidence"} style={{width: '100%', display: 'block'}} loading="lazy" />"""

replacement = """                <div className="exhibit__media" style={{marginTop: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'flex-start'}}>
                  {ex.media.map((m: any, mIdx: number) => (
                    <div key={mIdx} style={{marginBottom: '15px', flex: '1 1 300px'}}>
                      {m.type === 'image' || !m.type ? (
                        <div className="img-wrap" style={{border: '1px solid var(--atm-dim)', padding: '5px', background: 'rgba(0,0,0,0.2)'}}>
                          <img src={m.url} alt={m.alt || "Exhibit Evidence"} style={{width: '100%', display: 'block'}} loading="lazy" onClick={() => setLightbox({src: m.url, cap: m.alt})} style={{cursor: 'zoom-in', width: '100%', display: 'block'}} />"""

if target in content:
    content = content.replace(target, replacement)
    print("Updated renderer 8 - added cursor and flex styles")
else:
    print("Target not found")
    
with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
