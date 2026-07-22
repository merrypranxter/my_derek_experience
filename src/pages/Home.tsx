import { useEffect, useRef } from "react";
import { Link } from "react-router-dom";
import TTSButton from "../components/TTSButton";
import "../module.css";

const MODULES = [
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
  { id: "11", title: "FORENSICS", label: "NODE_771 — INDEPENDENT FORENSIC AUDIT" },
  { id: "12", title: "THE CUCKING", label: "ONE-WAY DISPLAY · TITLE WITHOUT DUTIES" }
];

const GLYPHS = 'ÐΣЯƎKΞ#/█▓?%';
const NAME = "DEREK";
const TRUTH = "an archive in thirteen modules. the record does not change.";
const LIE = "you are remembering it wrong.";

export default function Home() {
  const subjectRef = useRef<HTMLHeadingElement>(null);
  const chipsRef = useRef<(HTMLLIElement | null)[]>([]);
  const captionRef = useRef<HTMLParagraphElement>(null);
  const readoutRef = useRef<HTMLParagraphElement>(null);
  const orbitRef = useRef<HTMLUListElement>(null);
  const orbitPathRef = useRef<SVGEllipseElement>(null);

  useEffect(() => {
    document.title = `THE DEREK EXPERIENCE — Evidence Locker`;
    const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    // Set up letters
    if (!subjectRef.current) return;
    subjectRef.current.innerHTML = '';
    const letters = [...NAME].map(ch => {
      const s = document.createElement('span');
      s.className = 'letter';
      s.textContent = ch;
      s.setAttribute('aria-hidden', 'true');
      subjectRef.current!.appendChild(s);
      return s;
    });

    // 1. DIRECT: pointer proximity warp
    const state = letters.map(() => ({x:0, y:0, sk:0, sp:0}));
    let pointer: {x: number, y: number} | null = null;
    
    const handleMove = (e: PointerEvent) => { pointer = {x:e.clientX, y:e.clientY}; };
    const handleLeave = () => { pointer = null; };
    window.addEventListener('pointermove', handleMove, {passive:true});
    window.addEventListener('pointerleave', handleLeave);

    const RADIUS = 220, AMP = 26;
    let warpFrameId: number;
    function warpTick(){
      letters.forEach((el, i) => {
        const st = state[i];
        let tx=0, ty=0, tsk=0, tsp=1.4;
        if (pointer && !reduceMotion){
          const r = el.getBoundingClientRect();
          const cx = r.left + r.width/2, cy = r.top + r.height/2;
          const dx = cx - pointer.x, dy = cy - pointer.y;
          const d = Math.hypot(dx, dy);
          if (d < RADIUS){
            const f = (1 - d/RADIUS);
            const n = Math.max(d, 1);
            tx = (dx/n) * f * AMP;
            ty = (dy/n) * f * AMP * .6;
            tsk = (dx/n) * f * -14;
            tsp = 1.4 + f * 7;
          }
        }
        st.x += (tx-st.x)*.14; st.y += (ty-st.y)*.14;
        st.sk += (tsk-st.sk)*.14; st.sp += (tsp-st.sp)*.14;
        el.style.transform = `translate(${st.x.toFixed(2)}px, ${st.y.toFixed(2)}px) skewX(${st.sk.toFixed(2)}deg)`;
        el.style.setProperty('--split', st.sp.toFixed(2));
      });
      warpFrameId = requestAnimationFrame(warpTick);
    }
    warpFrameId = requestAnimationFrame(warpTick);

    // the ellipse: chips on a wide orbit, slow drift
    const chips = chipsRef.current.filter(Boolean) as HTMLLIElement[];
    let drift = 0;
    let driftPaused = false;
    const DRIFT_SPEED = (Math.PI * 2) / 95;

    function layoutEllipse(){
      const wide = matchMedia('(min-width: 720px)').matches;
      if (!wide){
        chips.forEach(c => { c.style.removeProperty('--x'); c.style.removeProperty('--y'); });
        return;
      }
      if (!orbitRef.current) return;
      const W = orbitRef.current.clientWidth, H = orbitRef.current.clientHeight;
      
      // Oval that fits on the page with nice breathing room around the title
      // Oval that fits on the page with nice breathing room around the title
      const a = Math.min(W * 0.44, W / 2 - 110);
      const b = Math.min(H * 0.40, H / 2 - 60);
      
      const path = orbitPathRef.current;
      if (path){ path.setAttribute('rx', a.toString()); path.setAttribute('ry', b.toString()); }
      
      chips.forEach((c, i) => {
        const t = (-90 + i * (360 / chips.length)) * Math.PI / 180 + drift;
        c.style.setProperty('--x', (Math.cos(t) * a).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(t) * b).toFixed(1) + 'px');
      });
    }
    
    let driftFrameId: number;
    function driftTick(){
      if (!reduceMotion && !driftPaused && !document.hidden){
        drift += DRIFT_SPEED / 60;
        layoutEllipse();
      }
      driftFrameId = requestAnimationFrame(driftTick);
    }
    window.addEventListener('resize', layoutEllipse);
    layoutEllipse();
    driftFrameId = requestAnimationFrame(driftTick);

    const onEnter = () => driftPaused = true;
    const onLeave = () => driftPaused = false;
    chips.forEach(c => {
      c.addEventListener('pointerenter', onEnter);
      c.addEventListener('pointerleave', onLeave);
      c.addEventListener('focus', onEnter);
      c.addEventListener('blur', onLeave);
    });

    const rnd = (n: number) => Math.floor(Math.random()*n);
    function ellipsePulse(){
      chips.forEach((c, i) => {
        setTimeout(() => {
          c.classList.remove('pulse'); void c.offsetWidth; c.classList.add('pulse');
        }, i * 75);
      });
    }

    // 2. AMBIENT: rare tears
    let tearTimeout: NodeJS.Timeout;
    function tearLetter(){
      if (!reduceMotion && !document.hidden){
        const el = letters[rnd(letters.length)];
        const orig = el.textContent || '';
        el.textContent = GLYPHS[rnd(GLYPHS.length)];
        el.classList.add('torn');
        setTimeout(() => { el.textContent = orig; el.classList.remove('torn'); }, 90 + rnd(80));
      }
      tearTimeout = setTimeout(tearLetter, 2500 + rnd(5000));
    }
    tearTimeout = setTimeout(tearLetter, 3000);

    // 3. OUTCOME: the name denies itself, the record corrects it
    let denialTimeout: NodeJS.Timeout;
    function denial(){
      if (!reduceMotion && !document.hidden){
        const scrambled = [...NAME].sort(() => Math.random() - .5).join('');
        letters.forEach((el, i) => { el.textContent = scrambled[i]; el.classList.add('torn'); });
        setTimeout(() => {
          letters.forEach((el, i) => { el.textContent = NAME[i]; el.classList.remove('torn'); });
          ellipsePulse();
        }, 160);
      }
      denialTimeout = setTimeout(denial, 18000 + rnd(14000));
    }
    denialTimeout = setTimeout(denial, 9000);

    // the caption gaslights, then recants
    let captionTimeout: NodeJS.Timeout;
    function captionLie(){
      if (!reduceMotion && !document.hidden && captionRef.current){
        captionRef.current.textContent = LIE;
        captionRef.current.classList.add('lie');
        setTimeout(() => { 
          if(captionRef.current) {
            captionRef.current.textContent = TRUTH; 
            captionRef.current.classList.remove('lie'); 
          }
        }, 340);
      }
      captionTimeout = setTimeout(captionLie, 22000 + rnd(16000));
    }
    captionTimeout = setTimeout(captionLie, 14000);

    // fit DEREK to the EXPERIENCE line
    function fitSubject(){
      const exp = document.querySelector('.experience');
      if (!exp || !subjectRef.current) return;
      const target = exp.getBoundingClientRect().width;
      if (!target) return;
      let size = parseFloat(getComputedStyle(subjectRef.current).fontSize);
      for (let i = 0; i < 3; i++){
        const w = subjectRef.current.getBoundingClientRect().width;
        if (!w) break;
        size = size * (target / w);
        subjectRef.current.style.fontSize = size.toFixed(1) + 'px';
      }
    }
    if (document.fonts && document.fonts.ready){ document.fonts.ready.then(fitSubject); }
    window.addEventListener('resize', fitSubject);
    fitSubject();

    return () => {
      window.removeEventListener('pointermove', handleMove);
      window.removeEventListener('pointerleave', handleLeave);
      window.removeEventListener('resize', layoutEllipse);
      window.removeEventListener('resize', fitSubject);
      cancelAnimationFrame(warpFrameId);
      cancelAnimationFrame(driftFrameId);
      clearTimeout(tearTimeout);
      clearTimeout(denialTimeout);
      clearTimeout(captionTimeout);
      chips.forEach(c => {
        c.removeEventListener('pointerenter', onEnter);
        c.removeEventListener('pointerleave', onLeave);
        c.removeEventListener('focus', onEnter);
        c.removeEventListener('blur', onLeave);
      });
    };
  }, []);

  const handleChipHover = (m: typeof MODULES[0]) => {
    if (readoutRef.current) {
      readoutRef.current.textContent = `▸ ${m.id} ${m.title} — ${m.label}`;
    }
    if (subjectRef.current) {
      const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
      if(!reduceMotion) subjectRef.current.style.filter = 'brightness(1.3) hue-rotate(-14deg) saturate(1.6)';
    }
  };

  const handleChipLeave = () => {
    if (readoutRef.current) readoutRef.current.textContent = '';
    if (subjectRef.current) subjectRef.current.style.filter = '';
  };

  return (
    <main className="stage">
      <ul className="orbit" id="orbit" ref={orbitRef}>
                <svg className="orbit__path" style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none' }} aria-hidden="true">
          <ellipse id="orbitPath" ref={orbitPathRef as any} cx="50%" cy="50%" rx="528" ry="328" fill="none" stroke="var(--atm-dim)" strokeOpacity=".38" strokeDasharray="2 7"/>
        </svg>

        <div className="docket relative">
          <TTSButton text={TRUTH} className="absolute -top-6 right-0" />
          <p className="filetag">EVIDENCE LOCKER · FILE <b>001</b> · SUBJECT</p>
          <h1 className="subject" id="subject" aria-label="DEREK" ref={subjectRef}>{NAME}</h1>
          <p className="experience">— THE <em>DEREK</em> EXPERIENCE —</p>
          <p className="caption" id="caption" ref={captionRef}>{TRUTH}</p>
          <p className="readout" id="readout" aria-live="polite" ref={readoutRef}></p>
        </div>

        {MODULES.map((m, i) => (
          <li className="chip" key={m.id} ref={el => { chipsRef.current[i] = el; }}>
            <Link 
              to={m.disabled ? `#m${m.id}` : `/module/${m.id}`}
              data-label={m.label}
              onPointerEnter={() => handleChipHover(m)}
              onPointerLeave={handleChipLeave}
              onFocus={() => handleChipHover(m)}
              onBlur={handleChipLeave}
            >
              <b>{m.id}</b>{m.title}
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}
