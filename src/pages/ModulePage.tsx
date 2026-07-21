import { useEffect, useState, useRef } from "react";
import { useParams, Link } from "react-router-dom";
import { motion, AnimatePresence } from "motion/react";

const MODULE_MAP: Record<string, string> = {
  "01": "MODULE_01_PROMISES",
  "02": "MODULE_02_WITHHOLDING",
  "03": "MODULE_03_RUG_PULLS",
  "04": "MODULE_04_GASLIGHTING_DARVO",
  "05": "MODULE_05_TRIANGULATION",
  "06": "MODULE_06_EXPLOITATION",
  "07": "MODULE_07_ERASURE",
};

interface MechanismNode {
  title: string;
  description: string;
}

interface Exhibit {
  num: string;
  name: string;
  source: string;
  quote: string;
  happened: string;
  analysis: string;
}

interface ParsedModule {
  id: string;
  title: string;
  projectCode: string;
  behavioralLabels: string[];
  coreObjective: string;
  mechanismDesc: string;
  mechanismNodes: MechanismNode[];
  exhibits: Exhibit[];
  impact: string[];
  rawYaml: string;
}

function parseModule(id: string, rawText: string): ParsedModule {
  const titleMatch = rawText.match(/^#\s+(.*)/m);
  const title = titleMatch ? titleMatch[1].replace(`MODULE ${id}: `, '') : 'Unknown Module';
  
  const projectCodeMatch = rawText.match(/\*\*Project Code:\*\*\s+`([^`]+)`/);
  const projectCode = projectCodeMatch ? projectCodeMatch[1] : '';
  
  const labelMatch = rawText.match(/\*\*Behavioral Label(?:s)?:\*\*\s+([^\n]+)/);
  const behavioralLabels = labelMatch ? labelMatch[1].split('/').map(s => s.trim()) : [];
  
  const objectiveMatch = rawText.match(/\*\*Core Objective:\*\*\s+([^\n]+)/);
  const coreObjective = objectiveMatch ? objectiveMatch[1] : '';

  // Extract mechanism list
  const mechNodes: MechanismNode[] = [];
  let mechanismDesc = "";
  const narrativeMatch = rawText.match(/## I\. THE NARRATIVE[^\n]*\n([\s\S]*?)(?=## II\.)/);
  if (narrativeMatch) {
    const lines = narrativeMatch[1].split('\n');
    let currentDesc = "";
    let inList = false;
    for (const line of lines) {
      const listMatch = line.match(/^\d+\.\s+\*\*([^\*]+)\*\*(.*)/);
      if (listMatch) {
        mechNodes.push({ title: listMatch[1].trim(), description: listMatch[2].trim() });
        inList = true;
      } else if (inList && line.trim().startsWith('-')) {
        // Handle list continuation if any
      } else if (!inList && line.trim() !== '') {
        currentDesc += line + " ";
      }
    }
    mechanismDesc = currentDesc.trim();
  }

  // Extract exhibits
  const exhibits: Exhibit[] = [];
  const exhibitsBlock = rawText.match(/## II\. DETAILED INSTANCE ANALYSIS([\s\S]*?)(?=## III\.)/);
  if (exhibitsBlock) {
    const instances = exhibitsBlock[1].split('### Instance ').filter(s => s.trim());
    for (const inst of instances) {
      const headerMatch = inst.match(/^([\d\.]+):\s+(.*)/);
      if (!headerMatch) continue;
      
      const ex: Exhibit = {
        num: headerMatch[1],
        name: headerMatch[2].trim().replace(/ —.*/, ''), // strip off quote from name if present
        source: '',
        quote: '',
        happened: '',
        analysis: ''
      };
      
      const lines = inst.split('\n');
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line.startsWith('- **Source:**')) ex.source = line.replace('- **Source:**', '').trim();
        if (line.startsWith('- **Direct Quote:**')) ex.quote = line.replace('- **Direct Quote:**', '').replace(/^"|"$/g, '').trim();
        if (line.startsWith('- **What happened:**')) ex.happened = line.replace('- **What happened:**', '').trim();
        if (line.startsWith('- **Analysis:**')) ex.analysis = line.replace('- **Analysis:**', '').trim();
      }
      exhibits.push(ex);
    }
  }

  // Extract impact
  const impact: string[] = [];
  const impactBlock = rawText.match(/## III\. DAMAGE ASSESSMENT([\s\S]*?)(?=## IV\.|$)/);
  if (impactBlock) {
    const lines = impactBlock[1].split('\n');
    for (const line of lines) {
      if (line.match(/^\d+\.\s/)) {
        impact.push(line.replace(/^\d+\.\s/, '').trim());
      }
    }
  }

  return {
    id,
    title,
    projectCode,
    behavioralLabels,
    coreObjective,
    mechanismDesc,
    mechanismNodes: mechNodes,
    exhibits,
    impact,
    rawYaml: rawText
  };
}

export default function ModulePage() {
  const { id } = useParams<{ id: string }>();
  const [parsed, setParsed] = useState<ParsedModule | null>(null);
  const mreadRef = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    if (!id || !MODULE_MAP[id]) return;
    const fetchMod = async () => {
      try {
        const res = await fetch(`/modules/${MODULE_MAP[id]}.md?t=${Date.now()}`);
        if (!res.ok) throw new Error("not found");
        const text = await res.text();
        setParsed(parseModule(id, text));
      } catch (e) {
        console.error(e);
      }
    };
    fetchMod();
  }, [id]);

  if (!parsed) return <div className="text-white p-12 font-mono">Loading module {id}...</div>;

  return (
    <div className="wrap">
      <Link className="back" to="/"><b>&lt;</b> RETURN TO LOCKER</Link>

      <header className="casehead">
        <p className="filetag">EVIDENCE LOCKER · MODULE <b>{id}</b> · <b>{parsed.projectCode}</b></p>
        <h1>{parsed.title}</h1>
        <p className="sub">( The Neurological Trigger )</p>
        <ul className="charges" aria-label="Behavioral charges">
          {parsed.behavioralLabels.map((lbl, idx) => (
            <li key={idx} style={{ '--tilt': `${(idx % 2 === 0 ? -1.2 : 0.8)}deg` } as any}>{lbl}</li>
          ))}
        </ul>
        <p className="objective">{parsed.coreObjective}</p>
      </header>

      {parsed.mechanismNodes.length > 0 && (
        <>
          <h2 className="sect"><b>I.</b> THE MECHANISM</h2>
          <p className="font-mono text-sm text-neutral-400 mb-6">{parsed.mechanismDesc}</p>
          <div className="mechanism" id="mechanism">
            {parsed.mechanismNodes.map((node, i) => (
              <div key={i} className="flex contents-node">
                <div 
                  className="mnode" 
                  tabIndex={0} 
                  onPointerEnter={() => { if(mreadRef.current) mreadRef.current.textContent = `▸ ${node.description}`; }}
                  onPointerLeave={() => { if(mreadRef.current) mreadRef.current.textContent = ''; }}
                >
                  <div className="n">{i + 1}</div>
                  <h3>{node.title}</h3>
                </div>
                {i < parsed.mechanismNodes.length - 1 && <div className="marrow">→</div>}
              </div>
            ))}
            <div className="mloop">⟲ <b>AND THE LOOP RESTARTS</b> — A SYSTEM IN MOTION</div>
            <p className="mread" ref={mreadRef} aria-live="polite"></p>
          </div>
        </>
      )}

      {parsed.exhibits.length > 0 && (
        <>
          <h2 className="sect"><b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD</h2>
          <div className="exhibits" id="exhibits">
            {parsed.exhibits.map((ex, i) => (
              <motion.article 
                key={i}
                initial={{ opacity: 0, y: 46 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-10%" }}
                transition={{ duration: 0.55, ease: [0.2, 0.8, 0.2, 1], delay: (i % 2) * 0.12 }}
                className="exhibit"
              >
                <div className="exhibit__top">
                  <span className="exhibit__num">EXHIBIT {ex.num}</span>
                  <span className="stamp" style={{ '--tilt': `${(i % 3 === 0 ? -2 : 1.5)}deg` } as any}>LOGGED</span>
                </div>
                <h3>{ex.name}</h3>
                <div className="ids">
                  <button className="eid" type="button">{ex.source.split('·')[0].trim()} <span className="d">· {ex.source.split('·')[1]?.trim() || ''}</span></button>
                </div>
                {ex.quote && <blockquote className="receipt">{ex.quote}</blockquote>}
                {ex.happened && <p className="note">{ex.happened}</p>}
                {ex.analysis && <p className="analysis"><b>ANALYSIS —</b> {ex.analysis.replace(/^\*\*(.*?)\*\*/, '')}</p>}
              </motion.article>
            ))}
          </div>
        </>
      )}

      {parsed.impact.length > 0 && (
        <>
          <h2 className="sect"><b>III.</b> DAMAGE ASSESSMENT</h2>
          <ol className="impact">
            {parsed.impact.map((imp, i) => {
              const boldMatch = imp.match(/^\*\*([^\*]+)\*\*(.*)/);
              if (boldMatch) {
                return <li key={i}><strong>{boldMatch[1]}</strong>{boldMatch[2]}</li>;
              }
              return <li key={i}>{imp}</li>;
            })}
          </ol>
        </>
      )}

      <h2 className="sect"><b>IV.</b> RAW DATA OUTPUT</h2>
      <details className="drawer mb-8">
        <summary>MACHINE-READABLE RECORD — RAW MARKDOWN</summary>
        <pre className="whitespace-pre-wrap">{parsed.rawYaml}</pre>
      </details>
      
      <div className="h-16"></div>
    </div>
  );
}
