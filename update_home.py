import re

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

target = """    <main className="relative z-10 min-h-screen flex items-center justify-center p-4">
      <ul className="orbit w-full max-w-[1200px] h-[88vh] max-h-[820px] relative m-0 p-0 list-none" ref={orbitRef}>
        <svg className="orbit__path absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 1200 820" preserveAspectRatio="none" aria-hidden="true">
          <ellipse id="orbitPath" cx="600" cy="410" rx="528" ry="328" style={{ fill:"none", stroke:"var(--atm-dim)", strokeOpacity:.38, strokeDasharray:"2 7" }} />
        </svg>

        <div className="docket !w-auto !h-auto !absolute !left-1/2 !top-1/2 -translate-x-1/2 -translate-y-1/2 z-10 text-center max-w-[62%] pointer-events-none">
          <p className="filetag">EVIDENCE LOCKER · FILE <b>001</b> · SUBJECT</p>
          <h1 className="subject inline-block whitespace-nowrap scale-y-[1.38] origin-[center_62%] pointer-events-auto" ref={subjectRef} aria-label="DEREK" style={{ fontSize: "100px", lineHeight: .9, letterSpacing: ".01em" }}>
            {Array.from(NAME).map((ch, i) => (
              <span key={i} className="letter" aria-hidden="true">{ch}</span>
            ))}
          </h1>
          <p className="experience !text-[clamp(.78rem,2.2vmin,1.05rem)] !mt-6">— THE <em>DEREK</em> EXPERIENCE —</p>
          <p className="caption !text-[clamp(.66rem,1.9vmin,.82rem)] !mt-[1.1rem]" ref={captionRef}>{TRUTH}</p>
          <p className="readout" ref={readoutRef} aria-live="polite"></p>
        </div>"""

replacement = """    <main className="stage">
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
        </div>"""

if target in content:
    content = content.replace(target, replacement)
else:
    print("TARGET NOT FOUND")

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)

