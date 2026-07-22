import re

with open('src/pages/ModulePage.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    "if (!parsed) return <div className=\"text-white p-12 font-mono\">Loading module {id}...</div>;",
    "if (!parsed && !MODULE_DATA[id]) return <div className=\"text-white p-12 font-mono\">EVIDENCE MISSING: Module {id} not found in the archive record.</div>;\n  if (!parsed) return <div className=\"text-white p-12 font-mono\">Loading module {id}...</div>;"
)

with open('src/pages/ModulePage.tsx', 'w') as f:
    f.write(content)
