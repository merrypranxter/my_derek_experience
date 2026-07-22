import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

target = """    function layoutEllipse(){
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

replacement = """    function layoutEllipse(){
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

if target in content:
    content = content.replace(target, replacement)
    with open("src/pages/Home.tsx", "w") as f:
        f.write(content)
    print("Replaced layoutEllipse successfully")
else:
    print("Target not found. Try regex or partial match.")

