with open('src/data/modules.ts', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# We will just replace all quote: "..." strings that have literal newlines in them if any.
# Specifically the one we just added:
bad_quote = '''quote: "Where he would just never let me see his face.'''
# Let's just find and replace the whole thing.

pattern = r'quote: "Where he would just never let me see his face\..*?He wouldn\'t even",'
# Actually let's just rewrite that entire block.

block_to_replace = r'''    { num: "2.4", status: "TESTIMONY",
      name: "The Goalpost & The Punishment",
      ids: \[\["TESTIMONY"\]\],
      quote: .*?,
      note: "Raw subject testimony recorded verbatim. No summary applied.",
      analysis: "The 'push the goalpost' mechanism combined with arbitrary rules \('if I mentioned it before it happened'\) creates a double-bind. It forces the victim to suppress their own excitement\/needs to 'earn' the reward, but the reward is intentionally withheld regardless, creating a cycle of self-blame and neurological distress, specifically weaponizing her neurodivergence \('literal torture'\)."\n    }'''

good_block = """    { num: "2.4", status: "TESTIMONY",
      name: "The Goalpost & The Punishment",
      ids: [["TESTIMONY"]],
      quote: `Where he would just never let me see his face. It's almost like he was trying to punish me. It's like he knew I thought he was beautiful and I had to earn it, but I never could. That's what it felt like.

He would do this thing where he'd push the goalpost where he'd tell me this date, but then there was a rule if I mentioned it before it happened. He would push the goalpost back a couple days, a couple weeks. I never knew, so I never knew when this was going to happen.

In my autistic brain, that's torture. That is torture to me. That was literal torture. It made my brain crazy. I had a lot of weird reactions when he would do that. It's very frustrating.

Just the push the goalpost thing. Why would he make me a promise and then never do the shit? It's not that hard and you didn't do it for other people, why wouldn't you do it for me? It just hurt my feelings. I had done anything for him. He wouldn't even`,
      note: "Raw subject testimony recorded verbatim. No summary applied.",
      analysis: "The 'push the goalpost' mechanism combined with arbitrary rules ('if I mentioned it before it happened') creates a double-bind. It forces the victim to suppress their own excitement/needs to 'earn' the reward, but the reward is intentionally withheld regardless, creating a cycle of self-blame and neurological distress, specifically weaponizing her neurodivergence ('literal torture')."
    }"""

content = re.sub(block_to_replace, good_block, content, flags=re.DOTALL)

with open('src/data/modules.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed modules.ts quotes")
