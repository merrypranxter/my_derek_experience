with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """              {ex.quote && <blockquote className="receipt">{ex.quote}</blockquote>}"""

replacement = """              {ex.image && (
                <div style={{ marginBottom: '1rem' }}>
                  <img src={ex.image} alt={ex.name} style={{ width: '100%', border: '1px solid var(--atm-paper-edge)', opacity: 0.95, filter: 'grayscale(0.15) contrast(1.1) sepia(0.2)' }} className="archival-scanlines" />
                </div>
              )}
              {ex.quote && <blockquote className="receipt">{ex.quote}</blockquote>}"""

content = content.replace(target, replacement)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)

print("Patched ModulePage.tsx")
