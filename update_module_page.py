import re
with open('src/pages/ModulePage.tsx', 'r') as f:
    content = f.read()

target = """        <p className="text-lg leading-relaxed text-neutral-300 border-l-2 border-cyan-500/50 pl-4 whitespace-pre-wrap">{parsed.objective}</p>
      </header>"""

replacement = """        <p className="text-lg leading-relaxed text-neutral-300 border-l-2 border-cyan-500/50 pl-4 whitespace-pre-wrap">{parsed.objective}</p>
        
        {parsed.epigraphs?.length > 0 && (
          <div className="mt-12 space-y-6">
            {parsed.epigraphs.map((epi: any, i: number) => (
              <blockquote key={i} className="border-l-4 border-magenta-500/50 pl-6 py-2 bg-gradient-to-r from-magenta-950/20 to-transparent">
                <p className="font-mono text-sm leading-relaxed text-neutral-300 mb-2 whitespace-pre-wrap break-words">{epi.text}</p>
                <footer className="text-xs tracking-[0.2em] uppercase font-bold text-magenta-400">
                  — {epi.who} <span className="text-neutral-500 mx-2">/</span> <span className="text-neutral-600">{epi.src}</span>
                </footer>
              </blockquote>
            ))}
          </div>
        )}
      </header>"""

# Using custom colors for the blockquote, so need to map magenta in tailwind configuration, or use standard colors like fuchsia
# Let's replace magenta with fuchsia which is standard in tailwind
replacement = replacement.replace("magenta", "fuchsia")

content = content.replace(target, replacement)

with open('src/pages/ModulePage.tsx', 'w') as f:
    f.write(content)
