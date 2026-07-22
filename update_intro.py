with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """            <section className="dsec">
              <h2>§ 2 — THE THING I ALWAYS WANTED</h2>
              <p>When he came into my life"""

replacement = """            <section className="dsec" style={{ display: 'flow-root' }}>
              <h2>§ 2 — THE THING I ALWAYS WANTED</h2>
              <figure style={{ float: 'right', marginLeft: '1.5rem', marginBottom: '1rem', width: '38%', minWidth: '220px' }}>
                <img 
                  src="https://storage.googleapis.com/astraltrash_other/derek/DUET_PARTNER_ORIGINAL.PNG" 
                  alt="Duet Partner Offer" 
                  style={{ width: '100%', border: '1px solid var(--atm-paper-edge)', opacity: 0.95, filter: 'grayscale(0.15) contrast(1.1) sepia(0.2)' }} 
                  className="archival-scanlines"
                />
                <figcaption className="docnote" style={{ marginTop: '0.4rem', borderTop: 'none', paddingTop: 0, textAlign: 'right', opacity: 0.8 }}>EXHIBIT: DUET_PARTNER_ORIGINAL</figcaption>
              </figure>
              <p>When he came into my life"""

content = content.replace(target, replacement)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)

print("Updated ModulePage.tsx")
