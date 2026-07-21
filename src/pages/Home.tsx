import { useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";

const MODULES = [
  { id: "01", title: "THE PROMISES", label: "LOVE-BOMBING / CONTRACT FANTASY" },
  { id: "02", title: "THE WITHHOLDING", label: "SCARCITY AS POWER" },
  { id: "03", title: "THE RUG-PULLS", label: "INTERMITTENT_REINFORCEMENT" },
  { id: "04", title: "THE GASLIGHTING", label: "DENY · ATTACK · REVERSE VICTIM & OFFENDER" },
  { id: "05", title: "THE TRIANGULATION", label: "THIRD-PARTY INSECURITY INDUCTION" },
  { id: "06", title: "THE EXPLOITATION", label: "EXTRACTION WITHOUT RECIPROCITY" },
  { id: "07", title: "THE ERASURE", label: "PUBLIC REPLACEMENT" },
  { id: "08", title: "THE LAST WORDS", label: "THE FINAL TRANSMISSION" },
  { id: "09", title: "THE RECORDINGS", label: "CAPTURED IN THE MOMENT" },
  { id: "10", title: "THE DUET ART", label: "WORK MADE FOR TWO" }
];

const GLYPHS = 'ÐΣЯƎKΞ#/█▓?%';
const NAME = "DEREK";
const TRUTH = "an archive in ten modules. the record does not change.";
const LIE = "you are remembering it wrong.";

export default function Home() {
  const navigate = useNavigate();
  const subjectRef = useRef<HTMLHeadingElement>(null);
  const chipsRef = useRef<(HTMLLIElement | null)[]>([]);
  const captionRef = useRef<HTMLParagraphElement>(null);
  const readoutRef = useRef<HTMLParagraphElement>(null);
  const orbitRef = useRef<HTMLUListElement>(null);

  useEffect(() => {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const subject = subjectRef.current;
    if (!subject) return;

    const letters = Array.from(subject.querySelectorAll('.letter')) as HTMLElement[];

    /* ---------- 1. DIRECT: pointer proximity warp ---------- */
    const state = letters.map(() => ({x:0, y:0, sk:0, sp:0}));
    let pointer: {x: number, y: number} | null = null;
    
    const onPointerMove = (e: PointerEvent) => { pointer = {x:e.clientX, y:e.clientY}; };
    const onPointerLeave = () => { pointer = null; };
    
    window.addEventListener('pointermove', onPointerMove, {passive:true});
    window.addEventListener('pointerleave', onPointerLeave);

    const RADIUS = 220, AMP = 26;
    let animFrame: number;
    
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
      animFrame = requestAnimationFrame(warpTick);
    }
    animFrame = requestAnimationFrame(warpTick);

    /* ---------- the ellipse: 10 chips, wide orbit, slow drift ---------- */
    let drift = 0;
    let driftPaused = false;
    const DRIFT_SPEED = (Math.PI * 2) / 95;
    let driftFrame: number;

    function layoutEllipse(){
      const orbit = orbitRef.current;
      if (!orbit) return;
      const wide = window.matchMedia('(min-width: 720px)').matches;
      if (!wide){
        chipsRef.current.forEach(c => { 
          if(c) {
            c.style.removeProperty('--x'); 
            c.style.removeProperty('--y'); 
          }
        });
        return;
      }
      const W = orbit.clientWidth, H = orbit.clientHeight;
      const a = Math.min(W * .44, W / 2 - 130);
      const b = Math.min(H * .40, H / 2 - 60);
      const path = document.getElementById('orbitPath');
      if (path){ path.setAttribute('rx', a.toString()); path.setAttribute('ry', b.toString()); }
      
      chipsRef.current.forEach((c, i) => {
        if (!c) return;
        const t = (-90 + i * (360 / MODULES.length)) * Math.PI / 180 + drift;
        c.style.setProperty('--x', (Math.cos(t) * a).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(t) * b).toFixed(1) + 'px');
      });
    }

    function driftTick(){
      if (!reduceMotion && !driftPaused && !document.hidden){
        drift += DRIFT_SPEED / 60;
        layoutEllipse();
      }
      driftFrame = requestAnimationFrame(driftTick);
    }
    window.addEventListener('resize', layoutEllipse);
    layoutEllipse();
    driftFrame = requestAnimationFrame(driftTick);

    const onChipEnter = () => { driftPaused = true; };
    const onChipLeave = () => { driftPaused = false; };

    chipsRef.current.forEach(c => {
      if(!c) return;
      c.addEventListener('pointerenter', onChipEnter);
      c.addEventListener('focus', onChipEnter, true);
      c.addEventListener('pointerleave', onChipLeave);
      c.addEventListener('blur', onChipLeave, true);
    });

    /* ---------- helpers ---------- */
    const rnd = (n: number) => Math.floor(Math.random()*n);
    function ellipsePulse(){
      chipsRef.current.forEach((c, i) => {
        if (!c) return;
        setTimeout(() => {
          c.classList.remove('pulse'); void c.offsetWidth; c.classList.add('pulse');
        }, i * 75);
      });
    }

    /* ---------- 2. AMBIENT: rare tears in individual letters ---------- */
    let tearTimeout: ReturnType<typeof setTimeout>;
    function tearLetter(){
      if (!reduceMotion && !document.hidden){
        const el = letters[rnd(letters.length)];
        if (el) {
          const orig = el.textContent || "";
          el.textContent = GLYPHS[rnd(GLYPHS.length)];
          el.classList.add('torn');
          setTimeout(() => { el.textContent = orig; el.classList.remove('torn'); }, 90 + rnd(80));
        }
      }
      tearTimeout = setTimeout(tearLetter, 2500 + rnd(5000));
    }
    tearTimeout = setTimeout(tearLetter, 3000);

    /* ---------- 3. OUTCOME: the name denies itself, then the archive corrects it ---------- */
    let denialTimeout: ReturnType<typeof setTimeout>;
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

    /* ---------- the caption gaslights, then recants ---------- */
    const caption = captionRef.current;
    let captionTimeout: ReturnType<typeof setTimeout>;
    function captionLie(){
      if (!reduceMotion && !document.hidden && caption){
        caption.textContent = LIE;
        caption.classList.add('lie');
        setTimeout(() => { caption.textContent = TRUTH; caption.classList.remove('lie'); }, 340);
      }
      captionTimeout = setTimeout(captionLie, 22000 + rnd(16000));
    }
    captionTimeout = setTimeout(captionLie, 14000);

    /* ---------- fit subject ---------- */
    function fitSubject(){
      const exp = document.querySelector('.experience') as HTMLElement;
      if (!exp || !subject) return;
      const target = exp.getBoundingClientRect().width;
      if (!target) return;
      let size = parseFloat(getComputedStyle(subject).fontSize);
      for (let i = 0; i < 3; i++){
        const w = subject.getBoundingClientRect().width;
        if (!w) break;
        size = size * (target / w);
        subject.style.fontSize = size.toFixed(1) + 'px';
      }
    }
    if (document.fonts && document.fonts.ready){ document.fonts.ready.then(fitSubject); }
    else { window.addEventListener('load', fitSubject); }
    window.addEventListener('resize', fitSubject);
    fitSubject();

    return () => {
      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerleave', onPointerLeave);
      window.removeEventListener('resize', layoutEllipse);
      window.removeEventListener('resize', fitSubject);
      window.removeEventListener('load', fitSubject);
      cancelAnimationFrame(animFrame);
      cancelAnimationFrame(driftFrame);
      clearTimeout(tearTimeout);
      clearTimeout(denialTimeout);
      clearTimeout(captionTimeout);
      chipsRef.current.forEach(c => {
        if(!c) return;
        c.removeEventListener('pointerenter', onChipEnter);
        c.removeEventListener('focus', onChipEnter, true);
        c.removeEventListener('pointerleave', onChipLeave);
        c.removeEventListener('blur', onChipLeave, true);
      });
    };
  }, []);

  return (
    <main className="stage">
      <ul className="orbit" id="orbit" ref={orbitRef}>
        <svg className="orbit__ring" viewBox="0 0 1200 820" preserveAspectRatio="none" aria-hidden="true">
          <ellipse id="orbitPath" cx="600" cy="410" rx="528" ry="328" style={{ fill:"none", stroke:"var(--atm-dim)", strokeOpacity:.38, strokeDasharray:"2 7" }} />
        </svg>

        <div className="docket">
          <div className="docket__inner">
            <p className="filetag">EVIDENCE LOCKER · FILE <b>001</b> · SUBJECT</p>
            <h1 className="subject" ref={subjectRef} aria-label="DEREK">
              {Array.from(NAME).map((ch, i) => (
                <span key={i} className="letter" aria-hidden="true">{ch}</span>
              ))}
            </h1>
            <p className="experience">— THE <em>DEREK</em> EXPERIENCE —</p>
            <p className="caption" ref={captionRef}>{TRUTH}</p>
            <p className="readout" ref={readoutRef} aria-live="polite"></p>
          </div>
        </div>

        {MODULES.map((mod, i) => (
          <li 
            key={mod.id} 
            className="chip" 
            ref={el => { chipsRef.current[i] = el; }}
          >
            <button 
              
              onClick={() => navigate(`/module/${mod.id}`)}
              onPointerEnter={() => {
                if (readoutRef.current) readoutRef.current.textContent = `▸ ${mod.id} ${mod.title} — ${mod.label}`;
                if (subjectRef.current) subjectRef.current.style.filter = 'brightness(1.3) hue-rotate(-14deg) saturate(1.6)';
              }}
              onFocus={() => {
                if (readoutRef.current) readoutRef.current.textContent = `▸ ${mod.id} ${mod.title} — ${mod.label}`;
                if (subjectRef.current) subjectRef.current.style.filter = 'brightness(1.3) hue-rotate(-14deg) saturate(1.6)';
              }}
              onPointerLeave={() => {
                if (readoutRef.current) readoutRef.current.textContent = '';
                if (subjectRef.current) subjectRef.current.style.filter = '';
              }}
              onBlur={() => {
                if (readoutRef.current) readoutRef.current.textContent = '';
                if (subjectRef.current) subjectRef.current.style.filter = '';
              }}
            >
              <b>{mod.id}</b>{mod.title}
            </button>
          </li>
        ))}
      </ul>
    </main>
  );
}
