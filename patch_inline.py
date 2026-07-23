import re

with open("/app/applet/src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """              <figure style={{ float: 'right', marginLeft: '1.5rem', marginBottom: '1rem', width: '38%', minWidth: '220px' }}>
                <img referrerPolicy="no-referrer" 
                  src="https://storage.googleapis.com/astraltrash_other/derek/DUET_PARTNER_ORIGINAL.PNG" 
                  alt="Duet Partner Offer" 
                  style={{ width: '100%', border: '1px solid var(--atm-paper-edge)', opacity: 0.95, filter: 'grayscale(0.15) contrast(1.1) sepia(0.2)' }} 
                  className="archival-scanlines"
                />"""

replacement = """              <figure style={{ float: 'right', marginLeft: '1.5rem', marginBottom: '1rem', width: '38%', minWidth: '220px', cursor: 'zoom-in' }} onClick={() => setLightbox({ src: 'https://storage.googleapis.com/astraltrash_other/derek/DUET_PARTNER_ORIGINAL.PNG', cap: '<b>THE ORIGINAL ASK</b> — “Will you be my officially unofficial video duet partner? 💍”' })}>
                <img referrerPolicy="no-referrer" 
                  src="https://storage.googleapis.com/astraltrash_other/derek/DUET_PARTNER_ORIGINAL.PNG" 
                  alt="Duet Partner Offer" 
                  style={{ width: '100%', border: '1px solid var(--atm-paper-edge)', opacity: 0.95, filter: 'grayscale(0.15) contrast(1.1) sepia(0.2)', transition: 'filter 0.2s', pointerEvents: 'none' }} 
                  className="archival-scanlines hover:filter-none"
                  loading="lazy"
                />"""

content = content.replace(target, replacement)

with open("/app/applet/src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
