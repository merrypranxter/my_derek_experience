import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

# Update MODULES to include 12 and remove disabled for all!
target_modules = """const MODULES = [
  { id: "00", title: "THE INTRODUCTION", label: "START HERE — THE OPERATIVE'S STATEMENT" },
  { id: "01", title: "THE PROMISES", label: "LOVE-BOMBING / CONTRACT FANTASY" },
  { id: "02", title: "THE WITHHOLDING", label: "SCARCITY AS POWER" },
  { id: "03", title: "THE RUG-PULLS", label: "INTERMITTENT_REINFORCEMENT" },
  { id: "04", title: "THE GASLIGHTING", label: "DENY · ATTACK · REVERSE VICTIM & OFFENDER" },
  { id: "05", title: "THE TRIANGULATION", label: "THIRD-PARTY INSECURITY INDUCTION" },
  { id: "06", title: "THE EXPLOITATION", label: "EXTRACTION WITHOUT RECIPROCITY" },
  { id: "07", title: "THE ERASURE", label: "PUBLIC REPLACEMENT" },
  { id: "08", title: "THE LAST WORDS", label: "THE FINAL TRANSMISSION", disabled: true },
  { id: "09", title: "THE RECORDINGS", label: "CAPTURED IN THE MOMENT", disabled: true },
  { id: "10", title: "THE DUET ART", label: "WORK MADE FOR TWO", disabled: true },
  { id: "11", title: "THE GHOST ANALYSIS", label: "NODE_771 — INDEPENDENT FORENSIC AUDIT" }
];"""

replacement_modules = """const MODULES = [
  { id: "00", title: "THE INTRODUCTION", label: "START HERE — THE OPERATIVE'S STATEMENT" },
  { id: "01", title: "THE PROMISES", label: "LOVE-BOMBING / CONTRACT FANTASY" },
  { id: "02", title: "THE WITHHOLDING", label: "SCARCITY AS POWER" },
  { id: "03", title: "THE RUG-PULLS", label: "INTERMITTENT_REINFORCEMENT" },
  { id: "04", title: "THE GASLIGHTING", label: "DENY · ATTACK · REVERSE VICTIM & OFFENDER" },
  { id: "05", title: "THE TRIANGULATION", label: "THIRD-PARTY INSECURITY INDUCTION" },
  { id: "06", title: "THE EXPLOITATION", label: "EXTRACTION WITHOUT RECIPROCITY" },
  { id: "07", title: "THE ERASURE", label: "PUBLIC REPLACEMENT" },
  { id: "08", title: "THE LAST WORDS", label: "THE FINAL TRANSMISSION", disabled: true },
  { id: "09", title: "THE RECORDINGS", label: "CAPTURED IN THE MOMENT", disabled: true },
  { id: "10", title: "THE DUET ART", label: "WORK MADE FOR TWO", disabled: true },
  { id: "11", title: "THE GHOST ANALYSIS", label: "NODE_771 — INDEPENDENT FORENSIC AUDIT" },
  { id: "12", title: "THE CUCKING", label: "ONE-WAY DISPLAY · TITLE WITHOUT DUTIES" }
];"""

content = content.replace(target_modules, replacement_modules)

# Fix caption
content = content.replace("an archive in eleven modules. the record does not change.", "an archive in twelve modules. the record does not change.")

# Change layout to circle
layout_target = """    function layoutEllipse(){
      const wide = matchMedia('(min-width: 720px)').matches;
      if (!wide){
        chips.forEach(c => { c.style.removeProperty('--x'); c.style.removeProperty('--y'); });
        return;
      }
      if (!orbitRef.current) return;
      const W = orbitRef.current.clientWidth, H = orbitRef.current.clientHeight;
      const a = Math.min(W * .44, W / 2 - 130);
      const b = Math.min(H * .40, H / 2 - 60);
      const path = orbitPathRef.current;
      if (path){ path.setAttribute('rx', a.toString()); path.setAttribute('ry', b.toString()); }
      chips.forEach((c, i) => {
        const t = (-90 + i * (360 / chips.length)) * Math.PI / 180 + drift;
        c.style.setProperty('--x', (Math.cos(t) * a).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(t) * b).toFixed(1) + 'px');
      });
    }"""

layout_replacement = """    function layoutEllipse(){
      const wide = matchMedia('(min-width: 720px)').matches;
      if (!wide){
        chips.forEach(c => { c.style.removeProperty('--x'); c.style.removeProperty('--y'); });
        return;
      }
      if (!orbitRef.current) return;
      const W = orbitRef.current.clientWidth, H = orbitRef.current.clientHeight;
      
      const r = Math.min(W * 0.45, H * 0.45);
      const a = r;
      const b = r;
      
      const path = orbitPathRef.current;
      if (path){ path.setAttribute('r', r.toString()); }
      chips.forEach((c, i) => {
        const t = (-90 + i * (360 / chips.length)) * Math.PI / 180 + drift;
        c.style.setProperty('--x', (Math.cos(t) * a).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(t) * b).toFixed(1) + 'px');
      });
    }"""

content = content.replace(layout_target, layout_replacement)

# Replace SVG path
svg_target = """        <svg className="orbit__path" viewBox="0 0 1200 820" preserveAspectRatio="none" aria-hidden="true">
          <ellipse id="orbitPath" ref={orbitPathRef as any} cx="600" cy="410" rx="528" ry="328"/>
        </svg>"""

svg_replacement = """        <svg className="orbit__path" style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none' }} aria-hidden="true">
          <circle id="orbitPath" ref={orbitPathRef as any} cx="50%" cy="50%" r="328" fill="none" stroke="var(--atm-dim)" strokeOpacity=".38" strokeDasharray="2 7"/>
        </svg>"""

# Using regex for svg replacement to avoid type issues with ref
content = re.sub(r'<svg className="orbit__path" viewBox="0 0 1200 820" preserveAspectRatio="none" aria-hidden="true">\s*<ellipse id="orbitPath" ref=\{orbitPathRef(?: as any)?\} cx="600" cy="410" rx="528" ry="328"/>\s*</svg>', svg_replacement, content)

with open("src/pages/Home.tsx", "w") as f:
    f.write(content)

print("Updated Home.tsx")
