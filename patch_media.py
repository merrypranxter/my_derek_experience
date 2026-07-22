import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Helper for Media Component
media_component = """
const MediaEmbed = ({ media, setLightbox }: { media: any, setLightbox: any }) => {
  if (!media) return null;
  if (media.type === 'video') {
    return (
      <div className="my-3 overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)]">
        <video src={media.url} autoPlay loop muted playsInline className="w-full h-auto" />
      </div>
    );
  }
  return (
    <div className="my-3 overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)] cursor-zoom-in hover:border-[var(--atm-cyan)] transition-colors" onClick={() => setLightbox({ src: media.url, cap: media.alt || '' })}>
      <img src={media.url} alt={media.alt || 'evidence'} className="w-full h-auto block filter saturate-90 hover:saturate-100 transition-all" referrerPolicy="no-referrer" />
    </div>
  );
};

export default function ModulePage() {
"""

content = content.replace("export default function ModulePage() {", media_component)

# Add media to addendum (.dsec)
content = content.replace(
    '<h2>{sec.title}</h2>',
    '<h2>{sec.title}</h2>\n                  <MediaEmbed media={sec.media} setLightbox={setLightbox} />'
)

# Add media to exhibits (.exhibit)
content = content.replace(
    '<h3>{ex.name}</h3>',
    '<h3>{ex.name}</h3>\n              <MediaEmbed media={ex.media} setLightbox={setLightbox} />'
)

# Add media to mechanisms (.mnode)
content = content.replace(
    '<h3>{n.title}</h3>',
    '<h3>{n.title}</h3>\n              <MediaEmbed media={n.media} setLightbox={setLightbox} />'
)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
