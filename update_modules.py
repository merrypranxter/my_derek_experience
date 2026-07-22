import re

with open('src/data/modules.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Module 00
intro_module = """
  '00': {
    id: "00", code: "MODULE_00_INTRODUCTION", title: "THE INTRODUCTION", sub: "( The Context )",
    labels: ["CONTEXT", "TESTIMONY"],
    objective: "To establish the baseline truth regarding Jay and the nature of the relationships before the mechanism of isolation was fully deployed.",
    epigraphs: [],
    mechanismTitle: "<b>I.</b> TESTIMONY",
    mechanism: [
      {
        title: "Subject Statement", 
        text: "I never had a problem with Jay. I never had a problem with Jay's existence. I was not jealous of Jay, not in the way she was jealous of me. I would have been completely and perfectly happy to have been friends with both of them because I understand that when we met, he was, like, I don't know, 38 years old. Sure, he had friends before me. Sure, some of them were probably female. Okay, so he had a friend who was a good friend before me and it was female. I wasn't trying to replace her. I was trying to be something else entirely. I wasn't trying to be romantic with him, I wasn't trying to be exclusive with him. We could have shared him. But she wouldn't let us. I realized she had me blocked one day and he went and he asked [TRUNCATED_DUE_TO_SYSTEM_LIMITS - more to be provided by user if needed]"
      }
    ],
    exhibitsTitle: "",
    exhibits: [],
    impact: [],
    yaml: `module: MODULE_00_INTRODUCTION\nstatus: INCOMPLETE_TRANSCRIPT`,
    prev: null,
    next: ["module01.html", "MODULE 01 — THE PROMISES"]
  },
"""

# We need to insert Module 00 right before Module 01 in the MODULE_DATA object.
content = content.replace("export const MODULE_DATA: Record<string, any> = {", "export const MODULE_DATA: Record<string, any> = {\n" + intro_module)
# We also need to update Module 01's prev to point to 00
content = content.replace("prev:null,\n  next:[\"module02.html\"", "prev:[\"module00.html\", \"MODULE 00 — THE INTRODUCTION\"],\n  next:[\"module02.html\"")

# For Module 02, we need to add the raw text as an exhibit or note.
withholding_notes = """
    { num: "2.4", status: "TESTIMONY",
      name: "The Goalpost & The Punishment",
      ids: [["TESTIMONY"]],
      quote: "Where he would just never let me see his face. It's almost like he was trying to punish me. It's like he knew I thought he was beautiful and I had to earn it, but I never could. That's what it felt like.\\n\\nHe would do this thing where he'd push the goalpost where he'd tell me this date, but then there was a rule if I mentioned it before it happened. He would push the goalpost back a couple days, a couple weeks. I never knew, so I never knew when this was going to happen.\\n\\nIn my autistic brain, that's torture. That is torture to me. That was literal torture. It made my brain crazy. I had a lot of weird reactions when he would do that. It's very frustrating.\\n\\nJust the push the goalpost thing. Why would he make me a promise and then never do the shit? It's not that hard and you didn't do it for other people, why wouldn't you do it for me? It just hurt my feelings. I had done anything for him. He wouldn't even",
      note: "Raw subject testimony recorded verbatim. No summary applied.",
      analysis: "The 'push the goalpost' mechanism combined with arbitrary rules ('if I mentioned it before it happened') creates a double-bind. It forces the victim to suppress their own excitement/needs to 'earn' the reward, but the reward is intentionally withheld regardless, creating a cycle of self-blame and neurological distress, specifically weaponizing her neurodivergence ('literal torture')."
    }"""

# Insert this into Module 02 exhibits.
# I will find the end of exhibits array for Module 02.
import re
# module 02 exhibits ends with:
# }
#   ],
#   impact:[
pattern = r"(name:\"The \\u201CRations\\u201D System\".*?analysis:.*?})\s*\]\s*,\s*impact:\["
replacement = r"\1," + withholding_notes + "\n  ],\n  impact:["

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('src/data/modules.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated modules.ts")
