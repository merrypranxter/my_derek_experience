import re

with open("/app/applet/src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """const MediaEmbed = ({ media, setLightbox }: { media: any, setLightbox: any }) => {
  if (!media) return null;
  if (media.type === 'video') {
    return (
      <div className="my-3 overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)]">
        <video src={media.url} controls playsInline className="w-full h-auto" />
      </div>
    );
  }
  return (
    <div className="my-3 overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)] cursor-zoom-in hover:border-[var(--atm-cyan)] transition-colors" onClick={() => setLightbox({ src: media.url, cap: media.alt || '' })}>
      <img src={media.url} alt={media.alt || 'evidence'} className="w-full h-auto block filter saturate-90 hover:saturate-100 transition-all" referrerPolicy="no-referrer" />
    </div>
  );
};"""

replacement = """const MediaEmbed = ({ media, setLightbox }: { media: any, setLightbox: any }) => {
  if (!media) return null;
  if (media.type === 'video') {
    return (
      <div className="my-5 w-full md:max-w-[50%] overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)]">
        <video src={media.url} controls playsInline className="w-full h-auto" />
      </div>
    );
  }
  return (
    <div className="my-5 w-full md:max-w-[50%] overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)] cursor-zoom-in hover:border-[var(--atm-cyan)] transition-colors" onClick={() => setLightbox({ src: media.url, cap: media.alt || '' })}>
      <img src={media.url} alt={media.alt || 'evidence'} loading="lazy" className="w-full h-auto block filter saturate-90 hover:saturate-100 transition-all" referrerPolicy="no-referrer" />
    </div>
  );
};"""

content = content.replace(target, replacement)

with open("/app/applet/src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
