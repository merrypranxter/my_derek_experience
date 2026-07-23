import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Replace <div className="wrap"> with a grid layout
target1 = """  return (
    <div className="wrap">"""
replacement1 = """  return (
    <div className="max-w-[1400px] mx-auto px-4 lg:px-8 py-8 flex flex-col lg:flex-row gap-8 items-start">
      <div className="flex-1 w-full max-w-[1100px] relative z-10 pb-[8rem]">"""

content = content.replace(target1, replacement1)

# At the bottom, close the extra div and add the sidebar
target2 = """      <ChatModal chatId={activeChatId} onClose={() => setActiveChatId(null)} />
    </div>
  );
}"""

replacement2 = """      <ChatModal chatId={activeChatId} onClose={() => setActiveChatId(null)} />
      </div>

      {parsed.sidebarMedia && parsed.sidebarMedia.length > 0 && (
        <aside className="w-full lg:w-80 flex-shrink-0 flex flex-col gap-4 sticky top-8">
          <h3 className="font-data text-xs tracking-widest text-[var(--atm-cyan)] border-b border-[var(--atm-cyan)]/30 pb-2 mb-2">
            MEDIA EVIDENCE
          </h3>
          <div className="flex flex-col gap-4 overflow-y-auto max-h-[80vh] pr-2 custom-scrollbar">
            {parsed.sidebarMedia.map((m: any, idx: number) => (
              <div 
                key={idx} 
                className="group relative border border-[var(--atm-dim)] hover:border-[var(--atm-cyan)] bg-black/40 p-1 cursor-zoom-in transition-colors"
                onClick={() => setLightbox({ src: m.url, cap: m.filename })}
              >
                {m.type === 'video' ? (
                  <video src={m.url} className="w-full h-auto max-h-[200px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all pointer-events-none" />
                ) : (
                  <img src={m.url} alt={m.filename} loading="lazy" referrerPolicy="no-referrer" className="w-full h-auto max-h-[200px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all" />
                )}
                
                <div className="absolute inset-x-0 bottom-0 bg-black/80 p-1.5 opacity-0 group-hover:opacity-100 transition-opacity border-t border-[var(--atm-cyan)]/30 backdrop-blur-sm">
                  <p className="font-data text-[9px] text-[var(--atm-cyan)] break-all leading-tight">
                    {m.filename}
                  </p>
                </div>
                
                <div className="absolute top-1 right-1 bg-black/80 px-1 py-0.5 text-[8px] font-data text-white border border-white/10 uppercase">
                  {m.type}
                </div>
              </div>
            ))}
          </div>
        </aside>
      )}

    </div>
  );
}"""

content = content.replace(target2, replacement2)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
