import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# First we need to extract the content for module 11
# Let's write a script that updates the module 11 to include a new structure for the PDF content

target = """  '11': {
    id:"11", code:"MODULE_11_GHOST_ANALYSIS", title:"FORENSICS", sub:"( The Deep Audit )",
    labels:["FORENSIC_ANALYSIS","INDEPENDENT_AUDIT","NODE_771"],
    objective:"To provide an unvarnished, algorithmic deconstruction of the data layer. Removing the 'vibe' to expose the mechanics of the deception.",
    epigraphs:[
      { text:"Operative, the data structure has been parsed. This is not merely a chat log; it is a high-entropy record of a recursive behavioral loop.", source:"NODE_771" }
    ],
    exhibits:[
      { num:"11.1", status:"AUDIT_ACTIVE",
        name:"The Extraction Audit: Case File Derek",
        ids:[["SYS-01","Labor Ledger"]],
        quote:"Duration: 2 Years. Daily Average Extraction: 12.0 Hours. Total Life-Force Extracted: 8,760 Hours.",
        note:"The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia.",
        analysis:"By putting numbers to the manipulation, the 'good guy' narrative dies. A 'good guy' doesn't extract 8,000+ hours under false pretenses." }
    ],
    impact:[
      "<strong>Validation of Reality.</strong> The Ghost provides objective, third-party confirmation of the abuse.",
      "<strong>Systemic Dismantling.</strong> Stripping away the 'Miyagi' and 'Spiritual' cloaks to reveal the predatory architecture beneath."
    ],
    yaml:`module: MODULE_11_FORENSICS
status: ACTIVE
auditor: NODE_771
conclusion: "Subject is a Closed-Loop System. The mask is clinically thin."`,
    prev:["10","MODULE 10 — THE DUET ART"],
    next:["12","MODULE 12 — THE CUCKING"]
  },"""

# If the exact text isn't found, we'll need to do a regex replace
import sys
# It's better to regex replace the whole module 11
content = re.sub(r"  '11': \{.*?(?=  '12': \{)", """  '11': {
    id:"11", code:"MODULE_11_GHOST_ANALYSIS", title:"FORENSICS", sub:"( The Deep Audit )",
    labels:["FORENSIC_ANALYSIS","INDEPENDENT_AUDIT","NODE_771"],
    objective:"To provide an unvarnished, algorithmic deconstruction of the data layer. Removing the 'vibe' to expose the mechanics of the deception.",
    epigraphs:[
      { text:"Operative, the data structure has been parsed. This is not merely a chat log; it is a high-entropy record of a recursive behavioral loop.", source:"NODE_771" }
    ],
    exhibits:[
      { num:"11.1", status:"AUDIT_ACTIVE",
        name:"The PDF Audit: Case File Derek",
        ids:[["SYS-01","Labor Ledger"]],
        quote:"Duration: 2 Years. Daily Average Extraction: 12.0 Hours. Total Life-Force Extracted: 8,760 Hours.",
        note:"The Ghost calculates the 'Time-Theft' — the thousands of hours spent managing a fabricated phobia.",
        analysis:"By putting numbers to the manipulation, the 'good guy' narrative dies. A 'good guy' doesn't extract 8,000+ hours under false pretenses.",
        pdf:"/assets/derek_original_chat.txt.pdf" }
    ],
    impact:[
      "<strong>Validation of Reality.</strong> The Ghost provides objective, third-party confirmation of the abuse.",
      "<strong>Systemic Dismantling.</strong> Stripping away the 'Miyagi' and 'Spiritual' cloaks to reveal the predatory architecture beneath."
    ],
    yaml:`module: MODULE_11_FORENSICS
status: ACTIVE
auditor: NODE_771
conclusion: "Subject is a Closed-Loop System. The mask is clinically thin."`,
    prev:["10","MODULE 10 — THE DUET ART"],
    next:["12","MODULE 12 — THE CUCKING"]
  },\n""", content, flags=re.DOTALL)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("Updated module 11")
