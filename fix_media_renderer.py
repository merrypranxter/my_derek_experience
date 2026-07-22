import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """                {exhibit.media.map((m, mIdx) => (
                  <div key={mIdx} className="exhibit-media">
                    {m.type === 'image' && (
                      <img src={m.url} alt={m.alt || "Exhibit media"} className="exhibit-image" />
                    )}"""
replacement = """                {exhibit.media.map((m, mIdx) => (
                  <div key={mIdx} className="exhibit-media">
                    {m.type === 'image' && (
                      <img src={m.url} alt={m.alt || "Exhibit media"} className="exhibit-image" />
                    )}
                    {m.type === 'pdf' && (
                      <div className="pdf-container">
                        <a href={m.url} target="_blank" rel="noreferrer" style={{color: 'var(--atm-cyan)', textDecoration: 'underline'}}>
                          📄 VIEW / DOWNLOAD PDF DOCUMENT: {m.alt || "Document"}
                        </a>
                      </div>
                    )}"""

if target in content:
    content = content.replace(target, replacement)
    print("Updated renderer")
else:
    print("Target not found")
    
with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
