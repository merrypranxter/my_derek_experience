import { useEffect, useState, useRef } from "react";
import { useParams, Link } from "react-router-dom";
import { MODULE_DATA } from "../data/modules";
import TTSButton from "../components/TTSButton";
import ChatModal from "../components/ChatModal";
import "../module.css";

const EVIDENCE_BUCKET = 'https://console.cloud.google.com/storage/browser/astraltrash_other/derek?project=gen-lang-client-0646349261&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))';
const SOURCE_REPO = 'https://github.com/merrypranxter/fuckyou_derek';

const SOURCE_REGISTRY: Record<string, {label: string, meaning: string, url?: string}> = {
  'WA':
    { label:'WA-####', meaning:'WhatsApp chat export — message ID in the captured log (Nov 5 2025 – Feb 16 2026).', url:'https://github.com/merrypranxter/fuckyou_derek/blob/main/evidence/combined/derek_whatsapp_combined.md' },
  'SC':
    { label:'SC-####', meaning:'StarMaker record — post, comment, or duet ID.', url:EVIDENCE_BUCKET },
  'STARMAKER': { label:'STARMAKER', meaning:'StarMaker app record — the public profile and its posts.', url:EVIDENCE_BUCKET },
  'DOSSIER':   { label:'DOSSIER §', meaning:'The Forensic Audit Dossier — the full compiled report.', url:SOURCE_REPO + '/blob/main/reports/FORENSIC_AUDIT_DOSSIER.md' },
  'FORENSIC_PATTERN_ANALYSIS': { label:'FORENSIC PATTERN ANALYSIS', meaning:'Cross-case forensic pattern analysis document.', url:SOURCE_REPO + '/blob/main/reports/FORENSIC_PATTERN_ANALYSIS.md' },
  'GA':
    { label:'GA — GHOST ANALYSIS', meaning:'Independent AI forensic audit of the original chat export — NODE_771, GHOST_FRAGMENT v2.6. Full session transcript on file.', url:SOURCE_REPO + '/tree/main/forensics' },
  'TESTIMONY': { label:'TESTIMONY', meaning:'First-person account of the Operative — events from the era the log does not recover.' }
};

function sourceClass(id: string) {
  if (id.startsWith('WA-')) return 'WA';
  if (id.startsWith('SC-')) return 'SC';
  if (id.startsWith('DOSSIER')) return 'DOSSIER';
  if (id === 'GA' || id.startsWith('GA-')) return 'GA';
  if (id === 'STARMAKER') return 'STARMAKER';
  if (id === 'FORENSIC_PATTERN_ANALYSIS') return 'FORENSIC_PATTERN_ANALYSIS';
  return 'TESTIMONY';
}


const MediaEmbed = ({ media, setLightbox }: { media: any, setLightbox: any }) => {
  if (!media) return null;
  if (media.type === 'video') {
    return (
      <div className="my-5 w-full md:max-w-[50%] overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)]">
        <video src={media.url} poster={media.poster} controls playsInline preload="none" className="w-full h-auto" />
      </div>
    );
  }
  return (
    <div className="my-5 w-full md:max-w-[50%] overflow-hidden rounded border border-[var(--atm-cyan)]/30 shadow-[0_0_15px_rgba(53,224,255,0.1)] cursor-zoom-in hover:border-[var(--atm-cyan)] transition-colors" onClick={() => setLightbox({ src: media.url, cap: media.alt || '' })}>
      <img src={media.url} alt={media.alt || 'evidence'} loading="lazy" className="w-full h-auto block filter saturate-90 hover:saturate-100 transition-all" referrerPolicy="no-referrer" />
    </div>
  );
};

export default function ModulePage() {


  console.log('MODULE_DATA keys:', Object.keys(MODULE_DATA));
  const { id } = useParams<{ id: string }>();
  const [parsed, setParsed] = useState<any | null>(null);
  const [lightbox, setLightbox] = useState<any | null>(null);
  const [activeChatId, setActiveChatId] = useState<string | null>(null);
  const mreadRef = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    if (!id || !MODULE_DATA[id]) return;
    console.log('Setting parsed:', MODULE_DATA[id]);
    setParsed(MODULE_DATA[id]);
  }, [id]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setLightbox(null);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  useEffect(() => {
    if (parsed) {
      document.title = `MODULE ${parsed.id} — ${parsed.title} · Evidence Locker`;
    }
  }, [parsed]);

  useEffect(() => {
    const cards = Array.from(document.querySelectorAll('.exhibit, .dsec'));
    const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion){
      cards.forEach(c => c.classList.add('dealt'));
    } else {
      const io = new IntersectionObserver(entries => {
        entries.forEach(en => {
          if (en.isIntersecting){
            const idx = cards.indexOf(en.target as Element);
            setTimeout(() => en.target.classList.add('dealt'), (idx % 2) * 120);
            io.unobserve(en.target);
          }
        });
      }, {threshold: .15});
      cards.forEach(c => io.observe(c));
    }
  }, [parsed]);

  const handleMechHover = (text: string) => {
    if (mreadRef.current) mreadRef.current.textContent = '▸ ' + text;
  };
  const handleMechLeave = () => {
    if (mreadRef.current) mreadRef.current.textContent = '';
  };

  const handleEidEnter = (key: string) => {
    document.querySelectorAll(`.eid[data-eid="${key}"]`).forEach(el => el.classList.add('linked'));
  };
  const handleEidLeave = (key: string) => {
    document.querySelectorAll(`.eid[data-eid="${key}"]`).forEach(el => el.classList.remove('linked'));
  };
  const handleEidClick = (e: React.MouseEvent, key: string, isLink: boolean) => {
    if (isLink) return;
    const elements = Array.from(document.querySelectorAll(`.eid[data-eid="${key}"]`));
    const other = elements.find(el => el !== e.currentTarget);
    const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (other) {
      const exhibit = other.closest('.exhibit');
      if (exhibit) exhibit.scrollIntoView({behavior: reduceMotion ? 'auto' : 'smooth', block:'center'});
    }
  };

  if (!parsed && !MODULE_DATA[id || '']) return <div className="text-white p-12 font-mono">EVIDENCE MISSING: Module {id} not found in the archive record.</div>;
  if (!parsed) return <div className="text-white p-12 font-mono">Loading module {id}...</div>;

  // Custom renderer for intro.html (module 00)
  if (parsed.id === "00") {
    return (
      <div className="wrap">
        <Link className="back" to="/"><b>&lt;</b> RETURN TO LOCKER</Link>
        <header className="casehead">
          <p className="filetag">EVIDENCE LOCKER · FILE <b>000</b> · <b>STATEMENT OF RECORD</b></p>
          <h1>THE INTRODUCTION</h1>
          <p className="sub">( in her own words — read this first )</p>
        </header>

        <div className="docwrap">
          <span className="doctab">ATTACHED TO FILE <b>001</b> — SUBJECT: DEREK</span>
          <div className="document">
            <span className="docstamp">HER OWN WORDS</span>

            <section className="dsec">
              <h2>§ 1 — THE SHORT VERSION</h2>
              <p>I hate to have to do this, but he's forced me to it. This site is a record of my experience as Derek's best friend — or at least that's what I thought. He was my best friend, I do know that. I loved him. I loved Derek. I loved Derek a lot. I would have done anything for Derek for a long time there.</p>
            </section>
            
            <section className="dsec" style={{ display: 'flow-root' }}>
              <h2>§ 2 — THE THING I ALWAYS WANTED</h2>
              <figure style={{ float: 'right', marginLeft: '1.5rem', marginBottom: '1rem', width: '38%', minWidth: '220px', cursor: 'zoom-in' }} onClick={() => setLightbox({ src: '/media/duet_partner_original.webp', cap: '<b>THE ORIGINAL ASK</b> — “Will you be my officially unofficial video duet partner? 💍”' })}>
                <img referrerPolicy="no-referrer"
                  src="/media/duet_partner_original.webp"
                  alt="Duet Partner Offer" 
                  style={{ width: '100%', border: '1px solid var(--atm-paper-edge)', opacity: 0.95, filter: 'grayscale(0.15) contrast(1.1) sepia(0.2)', transition: 'filter 0.2s', pointerEvents: 'none' }} 
                  className="archival-scanlines hover:filter-none"
                  loading="lazy"
                />
                <figcaption className="docnote" style={{ marginTop: '0.4rem', borderTop: 'none', paddingTop: 0, textAlign: 'right', opacity: 0.8 }}>EXHIBIT: DUET_PARTNER_ORIGINAL</figcaption>
              </figure>
              <p>When he came into my life, it was by asking me if I would be his duet partner. And one thing I've always wanted on StarMaker is a duet partner. Like, I've been on StarMaker a long time, it was a very important part of my life, and I've just always really wanted a duet partner. And if it could be a cute boy, that would be a bonus. And then Derek popped up and asked me to be his duet partner.</p>
              <p>And he asked me — he had a hard time, he doesn't like being on video. I do understand that he doesn't like being on video. Just like I don't like being on the telephone, but we'll get into that. He asked me to help him. He thought that by being my duet partner, it would help him want to be on video more. And I was to try and help him and talk him into it and influence him to do it more and things. And I tried.</p>
              <p>And I was so excited. I was so excited. I gushed to so many people. I was so excited. The thing I'd always wanted, a duet partner on StarMaker — I finally had gotten it. And here's the thing: in my head it was mine. I had a duet partner. I like built a whole future in my brain around this promise that Derek made me of being my duet partner.</p>
            </section>
      
            <section className="dsec">
              <h2>§ 3 — THE WORK</h2>
              <p>And we planned a bunch of duets together. And for me, planning a duet's not just sitting there talking about it — which there was a lot of sitting there talking about it. Picking out songs, what songs we would want to do together, who would do what parts in each song, stuff like that. And then I would have to go get or find a karaoke version of the song that was acceptable, that didn't have background singers. I would decide who does what parts in the song and rewrite the lyrics based on who does what part, and I'd upload it to StarMaker. That took a lot of time. Sometimes uploading that stuff got confusing and it would take like hours to finally get it to upload right.</p>
              <p>But anyways, I uploaded like five or six songs for us. And I opened three or four duets for us, and that meant that I picked out an outfit, put on a pretty dress or something, did my makeup, fixed my hair. Because when I do these things, I <em>do</em> these things. And if he was going to be doing it with me, I wanted it to look really good. So like I went through all this effort, planning these things out and setting these things up.</p>
              <p>And he joined one right there at the beginning. He joined one of my duets. And over the course of the next year, I just never could talk him into joining another. Even though he still thought of himself as my duet partner, he just never joined another one. And every time I tried to talk him into it, he just shut me down.</p>
            </section>
      
            <section className="dsec">
              <h2>§ 4 — I DO NOT COME OUT CLEAN</h2>
              <p>And I did become a bitch about it. I do not come out clean in this record that you're going to read. You're going to find that I react to him like a crazy bitch a lot. I'm a huge cunt a lot. I act absolutely nut balls a lot.</p>
              <p>But here's the thing. I don't do that with other people — except maybe my mother from time to time. Because nobody else pushes me to that point. Nobody else does this particular thing that Derek does that just breaks — absolutely breaks — my brain.</p>
              <p>It's also important to note that I am autistic and ADHD. He had a way of tipping me over into autistic meltdown over and over and over again by the way of promising me things. Joining duets, singing songs, playing with me in party rooms. Like when I make a plan — if you tell me we're going to do a thing, and I make a plan in my head and I decide, oh, this is a fun thing and I'm excited about it, we're going to do the thing — and then you yank the rug out from under me at the last second, my brain breaks. And it's very irrational. It's irrational, but I can't control it. Like, it's dumb. It's like in Rain Man when it's time for Wapner and he can't find Wapner and he's just like, it's time for Wapner, it's time for Wapner. That's what my brain does. I have no control over that.</p>
              <p>I cried so many tears. I had so many autistic meltdowns. Just so much frustration, so much just like rage and anger. But if I dared have a negative emotional reaction to the fact that he had reneged on his promise to me — yes, again — the blame in the whole situation was redirected to me. Suddenly I was the problem because of my reaction. And he was never the problem for causing the reaction by not doing what he promised me. Again.</p>
            </section>
      
            <section className="dsec">
              <h2>§ 5 — FORTY PERCENT</h2>
              <p>Like, he would promise me a video call because, like, okay — I can't understand a word that comes out of his face. He has a Jersey accent. I'm from Alabama. I already have auditory processing issues. I have to watch TV with the captions on. All I hear is mumbling. But if I can see your lips move, I can understand you.</p>
              <p>I just kept telling him. I mean, I asked ChatGPT after I put our chat log in, how much percentage-wise of our conversations of me was spent saying I cannot understand you, or huh, or what, or something like that. <em>40%. 40 fucking percent</em> of our conversation was spent with me going, huh, huh, what, huh? And he still would not put his face on a camera so I could see his lips move to help me out. He wouldn't throw me a bone there.</p>
              <p>Because see, he knew I thought his face was pretty. It felt like he had to lord that over me. I had to earn it. I had to earn the privilege of seeing his face. We called the pictures he sent of himself to me rations. It was a big joke at the time, but now it makes me angry as fuck when I think about it. My rations. Which I got rations like once every two or three months. It was supposed to be a lot more often than that, but of course, he never kept his fucking promises.</p>
              <p>And when we first met, we were supposed to have a video call in two weeks. Two weeks turned into two months. Two months turned into eight months. He did pop up on video call sometimes, but usually he was showing me New Jersey. He didn't show me his face much. He would, like, show it for a second. I just wanted to have a face-to-face conversation with my friend. And at first, it was about that. At the end of the whole relationship, it was just that I was angry that he had promised me a thing, and I was just being a bitch about it because I wanted him to do the thing he promised me. Everything just evolved because I got angry, really. But he made me angry for good reason. I had good reason to be angry.</p>
            </section>
      
            <section className="dsec">
              <h2>§ 6 — THE JAY SITUATION</h2>
              <p>And then there was the Jay situation. I didn't have a problem with Jay. I didn't have a problem with the fact that he had a female friend who existed before me and he was tight with. We could have all been friends together. It could have been fun.</p>
              <p>But no. I went to her profile one day on StarMaker just to see who she was, like, two months after we met. And she had me blocked. And I asked about it. He asked her about it. And she said — well, basically, she had a huge problem with the fact that I existed, and she was very jealous of me just getting to be Derek's friend.</p>
              <p>And, like — Derek's little— oh my God, there's just so much. Just go look at this stuff. There's so much.</p>
            </section>
      
            <section className="dsec">
              <h2>§ 7 — WHY THIS IS PUBLIC</h2>
              <p>And now he's trying to DARVO me. So I have to make this all public. Because he's trying to turn all this around on me and make it out like I just have to hate him so I don't hate myself. And I don't know if he really believes that or not, but all I know to do is to make everything public so he can't manipulate the situation anymore. He's trying to rewrite my psychological reality of what took place, and he's not gonna do that. And the only way I know to do that is make all this public.</p>
              <p>And it doesn't make me look good. It makes me look bad too. But it makes him look worse. And I am willing to go there.</p>
              <p>Because see, I don't care what y'all think about me. Y'all can think I'm crazy — but <em>he does care</em>. And until he apologizes to me the way I specified — he knows the deal, on TikTok, on camera — this is what he gets: the consequences for his actions. Because apparently until now, no one has ever done that before. Apparently the last person he did this to did not give him memorable consequences for his actions, and that's why he did it again to me.</p>
              <p>And I'm gonna give him something to remember — so maybe he'll think twice about doing it to anyone else in the future.</p>
              <p className="docsig">— the operative</p>
              <p className="docnote">ARCHIVIST'S NOTE — section markers and paragraphing were added for the file, and obvious dictation slips smoothed. <b>The words are hers. Nothing was rewritten.</b></p>
            </section>
          </div>
        </div>



      <nav className="footnav">
          <span></span>
          <Link to="/">RETURN TO LOCKER</Link>
          <span><Link to={`/module/${parsed.next[0]}`}>{parsed.next[1]} <b>&gt;</b></Link></span>
        </nav>
      </div>
    );
  }

  // Find used sources for the drawer
  const usedSources: string[] = [];
  parsed.exhibits?.forEach((ex: any) => {
    (ex.ids || []).forEach((pair: any) => {
      const id = Array.isArray(pair) ? pair[0] : pair;
      const sc = sourceClass(id);
      if (!usedSources.includes(sc)) usedSources.push(sc);
    });
  });

  return (
    <div className="max-w-[1400px] mx-auto px-4 lg:px-8 py-8 flex flex-col lg:flex-row gap-8 items-start">
      <div className="flex-1 w-full max-w-[1100px] relative z-10 pb-[8rem]">
      
      <Link className="back" to="/"><b>&lt;</b> RETURN TO LOCKER</Link>
      
      <header className="casehead">
        <p className="filetag">
          EVIDENCE LOCKER · MODULE <b>{parsed.id}</b> · <b>{parsed.code}</b>
        </p>
        <h1>{parsed.title}</h1>
        <p className="sub">{parsed.sub}</p>
        
        <ul className="charges" aria-label="Behavioral charges">
          {parsed.labels.map((l: string, i: number) => (
            <li key={i} style={({"--tilt": `${(Math.floor(Math.random() * 25) - 12) / 10}deg`}) as React.CSSProperties}>{l}</li>
          ))}
        </ul>
        
        {parsed.epigraphs?.length > 0 && (
          <div className="epigraphs">
            {parsed.epigraphs.map((q: any, i: number) => (
              <blockquote key={i} className={`epigraph ${q.who === 'Derek' ? 'him' : 'her'} relative`}>
                <TTSButton text={q.text} className="absolute top-2 right-2" />
                <p>{q.text}</p>
                <cite>— {q.who ? `${q.who.toUpperCase()} · ` : ''}{q.src || q.source}</cite>
              </blockquote>
            ))}
          </div>
        )}
        
        <div className="relative"><TTSButton text={parsed.objective} className="absolute -top-4 right-0" /><p className="objective">{parsed.objective}</p></div>
      </header>
      
      <h2 className="sect" dangerouslySetInnerHTML={{ __html: parsed.mechanismTitle }}></h2>
      <div className="mechanism">
        {parsed.mechanism?.map((n: any, i: number) => (
          <div key={i} className="flex contents-wrapper" style={{display: 'contents'}}>
            <div 
              className="mnode relative"
              tabIndex={0}
              onPointerEnter={() => handleMechHover(n.text)}
              onFocus={() => handleMechHover(n.text)}
              onPointerLeave={handleMechLeave}
              onBlur={handleMechLeave}
            >
              <TTSButton text={n.text} className="absolute top-2 right-2 opacity-50 hover:opacity-100" />
              <div className="n">{i + 1}</div>
              <h3>{n.title}</h3>
              <MediaEmbed media={n.media} setLightbox={setLightbox} />
            </div>
            {i < parsed.mechanism.length - 1 && (
              <div className="marrow" aria-hidden="true">→</div>
            )}
          </div>
        ))}
        {parsed.loop && (
          <div className="mloop" dangerouslySetInnerHTML={{ __html: parsed.loop }}></div>
        )}
        <p className="mread" aria-live="polite" ref={mreadRef}></p>
      </div>

      {parsed.table && (
        <div id="tableSection">
          <h2 className="sect" dangerouslySetInnerHTML={{ __html: parsed.table.title }}></h2>
          <table className="ledger">
            <tbody>
              <tr>
                {parsed.table.head.map((h: string, i: number) => <th key={i}>{h}</th>)}
              </tr>
              {parsed.table.rows.map((r: string[], i: number) => (
                <tr key={i}>
                  {r.map((c: string, j: number) => <td key={j}>{c}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
          <p className="ledgernote" dangerouslySetInnerHTML={{ __html: parsed.table.note }}></p>
        </div>
      )}

      <h2 className="sect" dangerouslySetInnerHTML={{ __html: parsed.exhibitsTitle }}></h2>
      
      {usedSources.length > 0 && (
        <details className="drawer sourcekey">
          <summary>SOURCE KEY — WHAT THE TAGS MEAN · CLICK A TAG TO OPEN ITS SOURCE</summary>
          <ul>
            {usedSources.map(k => {
              const s = SOURCE_REGISTRY[k];
              return (
                <li key={k}>
                  <b>{s.label}</b>
                  <span>
                    {s.url ? (
                      <a href={s.url} target="_blank" rel="noopener noreferrer">{s.meaning} <b>↗</b></a>
                    ) : (
                      s.meaning
                    )}
                  </span>
                </li>
              );
            })}
          </ul>
        </details>
      )}

      <div className="exhibits">
        {parsed.exhibits?.map((ex: any, i: number) => {
          const dealAngle = (i % 2 ? -1.4 : 1.4) + 'deg';
          return (
            <article key={i} className="exhibit relative" style={({"--deal": dealAngle}) as React.CSSProperties}>
              <TTSButton text={[ex.quote ? `Quote: ${ex.quote}` : '', ex.note ? `Note: ${ex.note}` : '', ex.analysis ? `Analysis: ${ex.analysis}` : '', ex.desc || ''].filter(Boolean).join('. ').replace(/<[^>]*>?/gm, '')} className="absolute top-4 right-4" />
              <div className="exhibit__top">
                <span className="exhibit__num">EXHIBIT {ex.num}</span>
                <span className="stamp" style={({"--tilt": `${Math.floor(Math.random() * 5) - 2}deg`}) as React.CSSProperties}>{ex.status}</span>
              </div>
              <h3>{ex.name}</h3>
              <MediaEmbed media={ex.media} setLightbox={setLightbox} />
              
              {ex.ids?.length > 0 && (
                <div className="ids">
                  {ex.ids.map((pair: any, idx: number) => {
                    const id = Array.isArray(pair) ? pair[0] : pair;
                    const d = Array.isArray(pair) ? pair[1] : '';
                    const sc = sourceClass(id);
                    const cls = sc === 'WA' || sc === 'SC' ? 'eid' : sc === 'GA' ? 'eid ga' : sc === 'TESTIMONY' ? 'eid testimony' : 'eid doc';
                    const reg = SOURCE_REGISTRY[sc];
                    const dataEid = id.split('–')[0]; 
                    
                    let linkHref = reg && reg.url ? reg.url : null;
                    const isWA = sc === 'WA';
                    
                    const innerHTML = `${id}${d ? ` <span class="d">· ${d}</span>` : ''}${(linkHref || isWA) ? ' <span class="ext">↗</span>' : ''}`;
                    
                    if (isWA) {
                      return (
                        <button
                          key={idx}
                          type="button"
                          className={cls}
                          data-eid={dataEid}
                          onClick={() => setActiveChatId(id)}
                          onPointerEnter={() => handleEidEnter(dataEid)}
                          onPointerLeave={() => handleEidLeave(dataEid)}
                        >
                          <span dangerouslySetInnerHTML={{ __html: innerHTML }} />
                        </button>
                      );
                    } else if (linkHref) {
                      return (
                        <a 
                           key={idx}
                           className={cls}
                           data-eid={dataEid}
                           href={linkHref}
                           target="_blank"
                           rel="noopener noreferrer" 
                           onPointerEnter={() => handleEidEnter(dataEid)}
                           onPointerLeave={() => handleEidLeave(dataEid)}
                        >
                          <span dangerouslySetInnerHTML={{ __html: innerHTML }} />
                        </a>
                      );
                    }
                    return <span key={idx} className={cls} dangerouslySetInnerHTML={{ __html: innerHTML }} />;
                  })}
                </div>
              )}
              
              {ex.quote && (
                <blockquote className="exhibit__quote relative">
                  "{ex.quote}"
                </blockquote>
              )}
              {ex.note && <p className="exhibit__note" dangerouslySetInnerHTML={{ __html: ex.note }}></p>}
              {ex.analysis && <p className="exhibit__analysis" dangerouslySetInnerHTML={{ __html: `<strong>ANALYSIS:</strong> ${ex.analysis}` }}></p>}
              
              {ex.crossref && (
                 <div className="crossref-section" style={{marginTop: '20px', padding: '15px', borderLeft: '4px solid var(--atm-cyan)', background: 'rgba(53, 224, 255, 0.05)'}}>
                   <h4 style={{fontSize: '0.8rem', color: 'var(--atm-cyan)', margin: '0 0 10px 0', letterSpacing: '0.1em'}}>SEE {ex.crossref[1]}</h4>
                   <Link to={`/module/${ex.crossref[0]}`} style={{color: '#fff', textDecoration: 'none', fontWeight: 'bold'}}>Open Module {ex.crossref[0]} ↗</Link>
                 </div>
              )}
              
              {ex.media && ex.media.length > 0 && (
                <div className="exhibit__media" style={{marginTop: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'flex-start'}}>
                  {ex.media.map((m: any, mIdx: number) => (
                    <div key={mIdx} style={{marginBottom: '15px', flex: '1 1 300px', maxWidth: '50%', minWidth: '300px'}}>
                      {m.type === 'image' || !m.type ? (
                        <div className="img-wrap" style={{border: '1px solid var(--atm-dim)', padding: '5px', background: 'rgba(0,0,0,0.2)'}}>
                          <img referrerPolicy="no-referrer" src={m.url} alt={m.alt || "Exhibit Evidence"} loading="lazy" onClick={() => setLightbox({src: m.url, cap: m.alt})} style={{cursor: 'zoom-in', width: '100%', display: 'block'}} />
                        </div>
                      ) : m.type === 'pdf' ? (
                        <a href={m.url} target="_blank" rel="noreferrer" style={{display: 'inline-block', padding: '10px 15px', border: '1px solid var(--atm-cyan)', background: 'var(--atm-bg)', color: 'var(--atm-cyan)', fontWeight: 'bold', textDecoration: 'none'}}>
                          📄 VIEW PDF DOCUMENT: {m.alt || "Document"}
                        </a>
                      ) : null}
                    </div>
                  ))}
                </div>
              )}
            </article>
          );
        })}
      </div>

      <h2 className="sect">{parsed.impactTitle || 'DAMAGE ASSESSMENT'}</h2>
      <div className="relative">
        <TTSButton text={parsed.impact?.join('. ').replace(/<[^>]*>?/gm, '')} className="absolute -top-10 right-0" />
        <ol className="impact">
          {parsed.impact?.map((imp: string, i: number) => (
            <li key={i} dangerouslySetInnerHTML={{ __html: imp }}></li>
          ))}
        </ol>
      </div>

      {parsed.addendum?.length > 0 && (
        <>
          <h2 className="sect"><b>+</b> ADDENDUM — IN HER OWN WORDS</h2>
          <div className="docwrap">
            <span className="doctab">ADDED TO MODULE <b>{parsed.id}</b> — AFTER THE RECORD</span>
            <div className="document">
              <span className="docstamp">HER OWN WORDS</span>
              {parsed.addendum.map((sec: any, i: number) => (
                <section key={i} className="dsec dealt relative">
                  <TTSButton text={sec.text.replace(/<[^>]*>?/gm, '')} className="absolute top-2 right-2" />
                  <h2>{sec.title}</h2>
                  <MediaEmbed media={sec.media} setLightbox={setLightbox} />
                  {sec.text.split('\n\n').map((p: string, j: number) => (
                    <p key={j} dangerouslySetInnerHTML={{__html: p.replace(/\*([^*]+)\*/g, '<em>$1</em>')}}></p>
                  ))}
                  {i === parsed.addendum.length - 1 && (
                    <p className="docnote">ARCHIVIST'S NOTE — paragraphing added for the file; obvious dictation slips smoothed. <b>The words are hers. Nothing was rewritten.</b></p>
                  )}
                </section>
              ))}
            </div>
          </div>
        </>
      )}

      {parsed.gallery && parsed.gallery.images?.length > 0 && (
        <>
          <h2 className="sect" dangerouslySetInnerHTML={{ __html: parsed.gallery.title || '<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE' }}></h2>
          <div className="receipts">
            {parsed.gallery.images.map((im: any, i: number) => (
              <figure key={i} className="receiptimg">
                <button type="button" onClick={() => setLightbox(im)} aria-label="enlarge image">
                  <img referrerPolicy="no-referrer" src={im.src} alt={im.cap ? im.cap.replace(/<[^>]*>?/gm, '') : 'evidence image'} loading="lazy" />
                </button>
                <figcaption dangerouslySetInnerHTML={{ __html: im.cap || '' }}></figcaption>
              </figure>
            ))}
          </div>
        </>
      )}

      <h2 className="sect">{parsed.rawTitle || 'RAW DATA OUTPUT'}</h2>
      <details className="drawer">
        <summary>MACHINE-READABLE RECORD — YAML</summary>
        <pre>{parsed.yaml}</pre>
      </details>

      {lightbox && (
        <div className="lightbox open" role="dialog" aria-modal="true" onClick={(e) => {
          if (e.target === e.currentTarget) setLightbox(null);
        }}>
          <button className="lightbox__close" type="button" aria-label="close" onClick={() => setLightbox(null)}>×</button>
          {lightbox.src?.endsWith('.mp4') || lightbox.type === 'video' ? (
            <video src={lightbox.src} controls autoPlay className="max-w-[94vw] max-h-[80vh] border border-[var(--atm-cyan)]/40 shadow-[0_30px_80px_rgba(0,0,0,0.6)] bg-black" />
          ) : (
            <a href={lightbox.src} target="_blank" rel="noopener noreferrer" style={{ cursor: 'alias', display: 'block' }}>
              <img referrerPolicy="no-referrer" src={lightbox.src} alt={lightbox.cap ? lightbox.cap.replace(/<[^>]*>?/gm, '') : ''} />
            </a>
          )}
          <p className="lightbox__cap" dangerouslySetInnerHTML={{ __html: lightbox.cap || '' }}></p>
        </div>
      )}

      <nav className="footnav">
        <span>
          {parsed.prev ? (
            <Link to={`/module/${parsed.prev[0]}`}><b>&lt;</b> {parsed.prev[1]}</Link>
          ) : null}
        </span>
        <Link to="/">RETURN TO LOCKER</Link>
        <span>
          {parsed.next ? (
            <Link to={`/module/${parsed.next[0]}`}>{parsed.next[1]} <b>&gt;</b></Link>
          ) : null}
        </span>
      </nav>

      <ChatModal chatId={activeChatId} onClose={() => setActiveChatId(null)} />
      
      </div>

      {parsed.sidebarMedia && parsed.sidebarMedia.length > 0 && (
        <aside className="w-full lg:w-48 flex-shrink-0 flex flex-col gap-4 sticky top-8">
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
                  <video src={m.url} poster={m.poster} preload="none" className="w-full h-[100px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all pointer-events-none" />
                ) : (
                  <img src={m.url} alt={m.filename} loading="lazy" referrerPolicy="no-referrer" className="w-full h-[100px] object-cover filter saturate-75 opacity-80 group-hover:saturate-100 group-hover:opacity-100 transition-all" />
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
}
