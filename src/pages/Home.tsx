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
];

const GLYPHS = 'ÐΣЯƎKΞ#/█▓?%';
const NAME = "DEREK";
const TRUTH = "an archive in seven modules. the record does not change.";
const LIE = "you are remembering it wrong.";

export default function Home() {
  const navigate = useNavigate();
  const subjectRef = useRef<HTMLHeadingElement>(null);
  const chipsRef = useRef<(HTMLLIElement | null)[]>([]);
  const captionRef = useRef<HTMLParagraphElement>(null);
  const readoutRef = useRef<HTMLParagraphElement>(null);
  const docketRef = useRef<HTMLDivElement>(null);

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
        let tx=0, ty=0, tsk=0, tsp=0;
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
            tsp = f * 7;
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

    /* ---------- helpers ---------- */
    const rnd = (n: number) => Math.floor(Math.random()*n);
    function pulseRing(){
      chipsRef.current.forEach((c, i) => {
        if (!c) return;
        setTimeout(() => {
          c.classList.remove('pulse'); void c.offsetWidth; c.classList.add('pulse');
        }, i * 60);
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
          pulseRing();
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

    /* ---------- orbit layout: modules on a 360° ring (wide) / stacked path (narrow) ---------- */
    const docket = docketRef.current;
    function layoutOrbit(){
      if (!docket) return;
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
      const r = docket.clientWidth / 2;
      chipsRef.current.forEach((c, i) => {
        if(!c) return;
        const a = (-90 + i * (360 / MODULES.length)) * Math.PI / 180;
        c.style.setProperty('--x', (Math.cos(a) * r).toFixed(1) + 'px');
        c.style.setProperty('--y', (Math.sin(a) * r).toFixed(1) + 'px');
      });
    }
    window.addEventListener('resize', layoutOrbit);
    layoutOrbit();

    return () => {
      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerleave', onPointerLeave);
      window.removeEventListener('resize', layoutOrbit);
      cancelAnimationFrame(animFrame);
      clearTimeout(tearTimeout);
      clearTimeout(denialTimeout);
      clearTimeout(captionTimeout);
    };
  }, []);

  return (
    <main className="stage">
      <div className="docket" ref={docketRef}>
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

          <ul className="orbit" id="orbit">
            <svg className="orbit__ring" viewBox="0 0 100 100" aria-hidden="true">
              <circle cx="50" cy="50" r="49"/>
            </svg>
            {MODULES.map((mod, i) => (
              <li 
                key={mod.id} 
                className="chip" 
                ref={el => { chipsRef.current[i] = el; }}
              >
                <button 
                  onClick={() => navigate(`/module/${mod.id}`)}
                  onPointerEnter={() => {
                    if (readoutRef.current) {
                      readoutRef.current.textContent = `▸ ${mod.id} ${mod.title} — ${mod.label}`;
                    }
                    if (subjectRef.current) {
                      subjectRef.current.style.filter = 'brightness(1.35)';
                    }
                  }}
                  onFocus={() => {
                    if (readoutRef.current) {
                      readoutRef.current.textContent = `▸ ${mod.id} ${mod.title} — ${mod.label}`;
                    }
                    if (subjectRef.current) {
                      subjectRef.current.style.filter = 'brightness(1.35)';
                    }
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
        </div>
      </main>
  );
}
