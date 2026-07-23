import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """      {lightbox && (
        <div className="lightbox open" role="dialog" aria-modal="true" onClick={(e) => {
          if (e.target === e.currentTarget) setLightbox(null);
        }}>
          <button className="lightbox__close" type="button" aria-label="close" onClick={() => setLightbox(null)}>×</button>
          <a href={lightbox.src} target="_blank" rel="noopener noreferrer" style={{ cursor: 'alias', display: 'block' }}>
            <img referrerPolicy="no-referrer" src={lightbox.src} alt={lightbox.cap ? lightbox.cap.replace(/<[^>]*>?/gm, '') : ''} />
          </a>
          <p className="lightbox__cap" dangerouslySetInnerHTML={{ __html: lightbox.cap || '' }}></p>
        </div>
      )}"""

replacement = """      {lightbox && (
        <div className="lightbox open" role="dialog" aria-modal="true" onClick={(e) => {
          if (e.target === e.currentTarget) setLightbox(null);
        }}>
          <button className="lightbox__close" type="button" aria-label="close" onClick={() => setLightbox(null)}>×</button>
          {lightbox.src?.endsWith('.mp4') || lightbox.type === 'video' ? (
            <video src={lightbox.src} controls autoPlay className="max-w-[94vw] max-h-[80vh] border border-[var(--atm-cyan)]/40 shadow-[0_30px_80px_rgba(0,0,0,0.6)] bg-black" />
          ) : (
            <a href={lightbox.src} target="_blank" rel="noopener noreferrer" style={{ cursor: 'alias', display: 'block' }}>
              <img referrerPolicy="no-referrer" src={lightbox.src} alt={lightbox.cap ? lightbox.cap.replace(/<[^>]*>?/gm, '') : ''} />
            </a>
          )}
          <p className="lightbox__cap" dangerouslySetInnerHTML={{ __html: lightbox.cap || '' }}></p>
        </div>
      )}"""

content = content.replace(target, replacement)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
