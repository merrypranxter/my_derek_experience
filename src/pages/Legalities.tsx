import { Link } from "react-router-dom";

export default function Legalities() {
  return (
    <div className="wrap text-neutral-400 font-data text-sm leading-relaxed pb-32">
      <Link className="back" to="/"><b>&lt;</b> RETURN TO LOCKER</Link>
      
      <header className="casehead">
        <p className="filetag">EVIDENCE LOCKER · LEGALITIES</p>
        <h1>LEGAL BATTLEFIELD ANALYSIS: NEW JERSEY EDITION</h1>
        <p className="sub">( Jurisdictional Considerations & Strategic Warfare )</p>
      </header>

      <div className="mt-12 space-y-12">
        <section>
          <h2 className="text-xl text-white font-subject tracking-widest mb-4 border-b border-white/20 pb-2">1. NEW JERSEY SPECIFIC LAWS</h2>
          <ul className="list-disc pl-6 space-y-2">
            <li><strong>Expectation of Privacy Laws</strong>: NJ recognizes limited expectation of privacy in electronic communications after transmission.</li>
            <li><strong>Consent Requirements</strong>: NJ is a <strong>two-party consent state</strong> for recording conversations (N.J.S.A. 2A:156A-4).</li>
            <li><strong>Defamation Laws</strong>: NJ has relatively plaintiff-friendly defamation laws.</li>
            <li><strong>Cyber Harassment</strong>: NJ has specific cyber-harassment statutes (N.J.S.A. 2C:33-4.1).</li>
            <li><strong>Revenge Porn</strong>: NJ criminalizes non-consensual pornography (N.J.S.A. 2C:14-9).</li>
          </ul>
        </section>

        <section>
          <h2 className="text-xl text-white font-subject tracking-widest mb-4 border-b border-white/20 pb-2">2. CONSENT & RECORDING LAWS</h2>
          <pre className="bg-black/50 p-4 border border-white/10 overflow-x-auto text-cyan-500 text-xs rounded">
            <code>{`// New Jersey Recording Consent Analysis
class NJConsentAnalyzer {
    constructor() {
        this.statutes = {
            twoPartyConsent: true,
            statute: "N.J.S.A. 2A:156A-4",
            penalty: "Third-degree crime (3-5 years prison)",
            exceptions: [
                "Law enforcement with warrant",
                "When parties reasonably expect to be recorded",
                "Public conversations with no expectation of privacy"
            ]
        };
    }
}`}</code>
          </pre>
        </section>

        <section>
          <h2 className="text-xl text-white font-subject tracking-widest mb-4 border-b border-white/20 pb-2">3. DEFAMATION RISK MITIGATION</h2>
          <div className="bg-black/30 border border-white/10 p-6">
            <h3 className="text-white mb-4">LEGAL PROTECTION LAYER</h3>
            <p className="mb-2"><strong>EVERY STATEMENT ON THIS SITE:</strong></p>
            <ul className="space-y-1 text-cyan-400 mb-6">
              <li>✅ Is 100% factual and verifiable</li>
              <li>✅ Is presented with supporting evidence</li>
              <li>✅ Contains no knowingly false information</li>
              <li>✅ Is presented for legitimate public interest</li>
              <li>✅ Does not constitute harassment</li>
            </ul>
            <div className="flex gap-2 text-xs font-bold">
              <span className="bg-cyan-900/40 text-cyan-300 px-2 py-1 border border-cyan-500/30">🔒 TRUTH-LOCKED</span>
              <span className="bg-cyan-900/40 text-cyan-300 px-2 py-1 border border-cyan-500/30">📁 EVIDENCE-BACKED</span>
              <span className="bg-cyan-900/40 text-cyan-300 px-2 py-1 border border-cyan-500/30">⚖️ LEGALLY DEFENSIBLE</span>
            </div>
          </div>
        </section>

        <section>
          <h2 className="text-xl text-white font-subject tracking-widest mb-4 border-b border-white/20 pb-2">4. ANONYMITY & JURISDICTIONAL SHIELDING</h2>
          <pre className="bg-black/50 p-4 border border-white/10 overflow-x-auto text-cyan-500 text-xs rounded">
            <code>{`// Jurisdictional Obfuscation System
class JurisdictionalShield {
    constructor() {
        this.protocols = {
            hosting: {
                primary: 'Netlify (US)',
                secondary: 'GitHub Pages (US)',
                tertiary: 'Vercel (US)',
                quaternary: 'Foreign hosting (outside NJ jurisdiction)'
            },
            dns: {
                useCloudflare: true,
                proxyThroughTor: false,
                multipleMirrors: true,
                dynamicIPRotation: false
            },
            cdn: {
                useMultipleCDNs: true,
                geoblocking: ['New Jersey'], // Block NJ IPs
                rateLimiting: true,
                DDoSProtection: true
            }
        };
    }
}`}</code>
          </pre>
        </section>

        <section>
          <h2 className="text-xl text-white font-subject tracking-widest mb-4 border-b border-white/20 pb-2">5. FIRST AMENDMENT PROTECTION STRATEGY</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="border border-white/10 p-4">
              <strong className="text-white block mb-2">🗽 It addresses matters of public concern</strong>
              <p className="text-xs">Documenting abusive behavior patterns serves public interest by warning others.</p>
            </div>
            <div className="border border-white/10 p-4">
              <strong className="text-white block mb-2">📰 It constitutes opinion and fair comment</strong>
              <p className="text-xs">Clearly labeled opinions about personal experiences are protected.</p>
            </div>
            <div className="border border-white/10 p-4">
              <strong className="text-white block mb-2">⚖️ Truth is an absolute defense against defamation</strong>
              <p className="text-xs">Every factual claim is supported by verifiable evidence.</p>
            </div>
            <div className="border border-white/10 p-4">
              <strong className="text-white block mb-2">🔒 It does not constitute "true threats" or harassment</strong>
              <p className="text-xs">The content documents past experiences without threatening future harm.</p>
            </div>
          </div>
        </section>

        <section>
          <h2 className="text-xl text-white font-subject tracking-widest mb-4 border-b border-white/20 pb-2">6. FINAL ASSESSMENT</h2>
          <div className="bg-[#05030f] border border-cyan-500/30 p-6 relative overflow-hidden">
            <div className="absolute top-0 left-0 w-1 h-full bg-cyan-500"></div>
            <p className="text-lg text-white mb-4"><strong>Your Legal Position is STRONG if:</strong></p>
            <ol className="list-decimal pl-6 space-y-2 mb-6">
              <li>All statements are factual and evidence-backed</li>
              <li>No non-consensual NJ recordings</li>
              <li>Personal identifiers are redacted</li>
              <li>Content serves public interest</li>
              <li>No ongoing harassment occurs</li>
            </ol>
            <p className="text-xs opacity-70">
              <strong>The Ultimate Protection:</strong> Truth backed by evidence, presented responsibly, for legitimate public interest purposes. New Jersey law actually PROTECTS victims speaking out about abuse—you just need to navigate the technicalities correctly.
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}
