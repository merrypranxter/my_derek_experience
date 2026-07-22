import re
with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Add gallery modal logic to ModulePage
gallery_component = """      <h2 className="sect">{parsed.rawTitle || 'RAW DATA OUTPUT'}</h2>"""

gallery_replacement = """
      {parsed.addendum?.length > 0 && (
        <>
          <h2 className="sect"><b>+</b> ADDENDUM — IN HER OWN WORDS</h2>
          <div className="docwrap">
            <span className="doctab">ADDED TO MODULE <b>{parsed.id}</b> — AFTER THE RECORD</span>
            <div className="document">
              <span className="docstamp">HER OWN WORDS</span>
              {parsed.addendum.map((sec: any, i: number) => (
                <section key={i} className="dsec dealt">
                  <h2>{sec.title}</h2>
                  {sec.text.split('\\n\\n').map((p: string, j: number) => (
                    <p key={j} dangerouslySetInnerHTML={{__html: p.replace(/\\*([^*]+)\\*/g, '<em>$1</em>')}}></p>
                  ))}
                  {i === parsed.addendum.length - 1 && (
                    <p className="docnote">ARCHIVIST'S NOTE — paragraphing added for the file; obvious dictation slips smoothed. <b>The words are hers. Nothing was rewritten.</b></p>
                  )}
                </section>
              ))}
            </div>
          </div>
        </>
      )}

      {parsed.gallery && parsed.gallery.images?.length > 0 && (
        <>
          <h2 className="sect" dangerouslySetInnerHTML={{ __html: parsed.gallery.title || '<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE' }}></h2>
          <div className="receipts">
            {parsed.gallery.images.map((im: any, i: number) => (
              <figure key={i} className="receiptimg">
                <button type="button" onClick={() => setLightbox(im)} aria-label="enlarge image">
                  <img src={im.src} alt={im.cap ? im.cap.replace(/<[^>]*>?/gm, '') : 'evidence image'} loading="lazy" />
                </button>
                <figcaption dangerouslySetInnerHTML={{ __html: im.cap || '' }}></figcaption>
              </figure>
            ))}
          </div>
        </>
      )}

      <h2 className="sect">{parsed.rawTitle || 'RAW DATA OUTPUT'}</h2>"""

content = content.replace(gallery_component, gallery_replacement)

# Add lightbox state
content = content.replace("const [parsed, setParsed] = useState<any | null>(null);", "const [parsed, setParsed] = useState<any | null>(null);\n  const [lightbox, setLightbox] = useState<any | null>(null);")

# Add lightbox rendering at the bottom before closing div
lightbox_render = """      <nav className="footnav">"""
lightbox_replacement = """      {lightbox && (
        <div className="lightbox open" role="dialog" aria-modal="true" onClick={(e) => {
          if (e.target === e.currentTarget) setLightbox(null);
        }}>
          <button className="lightbox__close" type="button" aria-label="close" onClick={() => setLightbox(null)}>×</button>
          <img src={lightbox.src} alt={lightbox.cap ? lightbox.cap.replace(/<[^>]*>?/gm, '') : ''} />
          <p className="lightbox__cap" dangerouslySetInnerHTML={{ __html: lightbox.cap || '' }}></p>
        </div>
      )}

      <nav className="footnav">"""
content = content.replace(lightbox_render, lightbox_replacement)

# Add keyboard handler for lightbox escape
content = content.replace("  useEffect(() => {\n    if (!id || !MODULE_DATA[id]) return;\n    setParsed(MODULE_DATA[id]);\n  }, [id]);", """  useEffect(() => {
    if (!id || !MODULE_DATA[id]) return;
    setParsed(MODULE_DATA[id]);
  }, [id]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setLightbox(null);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);""")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
print("fixed module page rendering")
