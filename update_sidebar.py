with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

old_sidebar = '''        <aside className="w-full lg:w-80 flex-shrink-0 flex flex-col gap-4 sticky top-8">
          <h3 className="font-data text-xs tracking-widest text-[var(--atm-cyan)] border-b border-[var(--atm-cyan)]/30 pb-2 mb-2">
            MEDIA EVIDENCE
          </h3>
          <div className="flex flex-col gap-4 overflow-y-auto max-h-[80vh] pr-2 custom-scrollbar">
            {parsed.sidebarMedia.map((m: any, idx: number) => (
              <div 
                key={idx} 
                className="group relative border border-[var(--atm-dim)] hover:border-[var(--atm-cyan)] bg-black/40 p-1 cursor-zoom-in transition-colors"
                onClick={() => setLightbox({ src: m.url, cap: m.filename, type: m.type })}
              >
                {m.type === 'video' ? (
                  <video src={m.url} className="w-full h-auto max-h-[200px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all pointer-events-none" />
                ) : (
                  <img src={m.url} alt={m.filename} loading="lazy" referrerPolicy="no-referrer" className="w-full h-auto max-h-[200px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all" />
                )}'''

new_sidebar = '''        <aside className="w-full lg:w-48 flex-shrink-0 flex flex-col gap-4 sticky top-8">
          <h3 className="font-data text-[10px] tracking-widest text-[var(--atm-cyan)] border-b border-[var(--atm-cyan)]/30 pb-2 mb-2">
            MEDIA EVIDENCE
          </h3>
          <div className="flex flex-row lg:flex-col gap-2 overflow-auto lg:max-h-[85vh] pb-4 lg:pb-0 pr-2 custom-scrollbar">
            {parsed.sidebarMedia.map((m: any, idx: number) => (
              <div 
                key={idx} 
                className="group relative border border-[var(--atm-dim)] hover:border-[var(--atm-cyan)] bg-black/40 p-1 cursor-zoom-in transition-colors w-[120px] lg:w-full flex-shrink-0"
                onClick={() => setLightbox({ src: m.url, cap: m.filename, type: m.type })}
              >
                {m.type === 'video' ? (
                  <video src={m.url} preload="none" className="w-full h-[100px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all pointer-events-none" />
                ) : (
                  <img src={m.url} alt={m.filename} loading="lazy" referrerPolicy="no-referrer" className="w-full h-[100px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all" />
                )}'''

content = content.replace(old_sidebar, new_sidebar)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
