import os

with open('public/modules/MODULE_05_TRIANGULATION.md', 'r') as f:
    content = f.read()

target = """- **The Behavior:** Sexual/flirtatious messages directed at Jay, contrasted against the framing that Merry's own freely offered intimacy was special and exclusive.
- **Source:** `user_testimony`; Forensic Pattern Analysis
- **Analysis:** The exclusivity was the product being sold to Merry (MODULE_01's "unofficially official" bond). The contrast is the invoice: the same currency was circulating elsewhere. Discovery of it doesn't end the arrangement — it intensifies it, because now she must *compete*."""

replacement = """- **Source:** `user_testimony`
- **What happened:** Merry was initially open to friendship with Jay, but Jay blocked her out of jealousy. The core conflict was over a promise Derek made: to rotate representation on his StarMaker profile, giving partners five days at a time. Merry requested her five days of representation to reflect the emotional labor she was investing. He never fulfilled this rotation, eventually stating: "she has cancer, and you can have it when she dies."
- **Analysis:** The conflict was not about jealousy, but a broken promise and hostile gatekeeping. Derek dangled a promise of public representation (the "five days"), failed to enforce the rotation, and allowed the third party to act as a hostile barrier. Merry’s resulting frustration was then mischaracterized as being "jealous," masking the underlying issue of unreciprocated emotional labor and withdrawn promises."""

content = content.replace(target, replacement)

with open('public/modules/MODULE_05_TRIANGULATION.md', 'w') as f:
    f.write(content)
