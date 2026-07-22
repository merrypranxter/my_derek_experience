import re

with open("src/pages/VisualEvidence.tsx", "r") as f:
    content = f.read()

# Add import
content = content.replace('import evidenceFiles from "../data/evidenceFiles.json";', 'import evidenceFiles from "../data/evidenceFiles.json";\nimport TTSButton from "../components/TTSButton";')

target = """          <p className="text-neutral-400 font-data text-sm max-w-2xl mb-12 border-l border-cyan-500/50 pl-4">
            Direct feed from cloud storage established. The images below contain receipts, chat logs, and art files provided for cross-referencing.
            <br/><br/>
            <span className="text-cyan-400">Notice:</span> Original bucket filenames are preserved below each asset.
          </p>"""

replacement = """          <div className="relative">
            <TTSButton text="Direct feed from cloud storage established. The images below contain receipts, chat logs, and art files provided for cross-referencing. Notice: Original bucket filenames are preserved below each asset." className="absolute -top-4 -left-4" />
            <p className="text-neutral-400 font-data text-sm max-w-2xl mb-12 border-l border-cyan-500/50 pl-4 relative">
              Direct feed from cloud storage established. The images below contain receipts, chat logs, and art files provided for cross-referencing.
              <br/><br/>
              <span className="text-cyan-400">Notice:</span> Original bucket filenames are preserved below each asset.
            </p>
          </div>"""

if target in content:
    content = content.replace(target, replacement)
    print("Patched VisualEvidence.tsx")
else:
    print("Target not found")

with open("src/pages/VisualEvidence.tsx", "w") as f:
    f.write(content)
