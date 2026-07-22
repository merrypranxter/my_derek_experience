import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

# Change layoutEllipse back to an ellipse
layout_target = """    function layoutEllipse(){
      const wide = matchMedia('(min-width: 720px)').matches;
      if (!wide){
        chips.forEach(c => { c.style.removeProperty('--x'); c.style.removeProperty('--y'); });
        return;
      }
      if (!orbitRef.current) return;
      const W = orbitRef.current.clientWidth;
      
      // Make it a large circle so it's not crammed in the center
      const r = Math.min(W * 0.42, 480);
      
      const path = orbitPathRef.current;
      if (path){ path.setAttribute('r', r.toString()); }
      
      chips.forEach((c, i) => {
        const t = (-90 + i * (360 / chips.length)) * Math.PI / 180 + drift;
        c.style.setProperty('--x', (Math.cos(t) * r).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(t) * r).toFixed(1) + 'px');
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
      
      const a = Math.min(W * .44, W / 2 - 110);
      const b = Math.min(H * .42, H / 2 - 60);
      
      const path = orbitPathRef.current;
      if (path){ path.setAttribute('rx', a.toString()); path.setAttribute('ry', b.toString()); }
      
      chips.forEach((c, i) => {
        const t = (-90 + i * (360 / chips.length)) * Math.PI / 180 + drift;
        c.style.setProperty('--x', (Math.cos(t) * a).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(t) * b).toFixed(1) + 'px');
      });
    }"""

if layout_target in content:
    content = content.replace(layout_target, layout_replacement)
else:
    print("Could not find layoutEllipse to replace.")

# Replace SVG circle with ellipse
svg_target = """        <svg className="orbit__path" style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none' }} aria-hidden="true">
          <circle id="orbitPath" ref={orbitPathRef as any} cx="50%" cy="50%" r="328" fill="none" stroke="var(--atm-dim)" strokeOpacity=".38" strokeDasharray="2 7"/>
        </svg>"""

svg_replacement = """        <svg className="orbit__path" style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none' }} aria-hidden="true">
          <ellipse id="orbitPath" ref={orbitPathRef as any} cx="50%" cy="50%" rx="528" ry="328" fill="none" stroke="var(--atm-dim)" strokeOpacity=".38" strokeDasharray="2 7"/>
        </svg>"""

if svg_target in content:
    content = content.replace(svg_target, svg_replacement)
else:
    # Try regex fallback
    content = re.sub(r'<svg className="orbit__path" style=\{\{ position: \'absolute\', inset: 0, width: \'100%\', height: \'100%\', pointerEvents: \'none\' \}\} aria-hidden="true">\s*<circle id="orbitPath" ref=\{orbitPathRef(?: as any)?\} cx="50%" cy="50%" r="[^"]*" fill="none" stroke="var\(--atm-dim\)" strokeOpacity="\.38" strokeDasharray="2 7"/>\s*</svg>', svg_replacement, content)

with open("src/pages/Home.tsx", "w") as f:
    f.write(content)

print("Restored oval layout")
