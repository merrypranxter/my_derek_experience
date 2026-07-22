import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Add a section to Module 12 to show the art images
target3 = """      { num:"12.4", status:"TITLE_RETENTION",
        name:"“But I'm Your Duet Partner”",
        ids:[["TESTIMONY"]],
        note:"Months in, as she is already letting go of the relationship, he re-invokes the title: but I'm your duet partner. A title he never once performed after the first duet.",
        analysis:"He never performed the partnership — but he never released the title either, because the title was the pump. As long as she believed she held it, the joins, the art, the gifts, and the public display kept flowing. Retaining the name while declining the duties is not a relationship status; it is a billing arrangement.",
        crossref:["01","MODULE_01 — THE PROMISES"] },"""

replacement3 = """      { num:"12.4", status:"TITLE_RETENTION",
        name:"“But I'm Your Duet Partner”",
        ids:[["TESTIMONY"]],
        note:"Months in, as she is already letting go of the relationship, he re-invokes the title: but I'm your duet partner. A title he never once performed after the first duet.",
        analysis:"He never performed the partnership — but he never released the title either, because the title was the pump. As long as she believed she held it, the joins, the art, the gifts, and the public display kept flowing. Retaining the name while declining the duties is not a relationship status; it is a billing arrangement.",
        crossref:["01","MODULE_01 — THE PROMISES"] },
      { num:"12.5", status:"ARTIFACT_RECOVERED",
        name:"The Extracted Art",
        ids:[["ART-01","Uncompensated Labor"]],
        quote:"[Visual documentation of the art assets created by the Operative for the Subject.]",
        note:"While he 'could not' sing with her, he happily accepted the labor, time, and talent she poured into creating custom artwork for him. The extraction was absolute.",
        analysis:"This proves the relationship was transactional, but entirely one-sided. He consumed her creative output while systematically denying her the one shared experience she requested.",
        media: [
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_1.jpeg", alt: "Art created for Derek 1" },
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_2.jpg", alt: "Art created for Derek 2" }
        ] }"""

if target3 in content:
    content = content.replace(target3, replacement3)
    print("Added art images to Module 12")
else:
    print("Target 3 not found")

with open("src/data/modules.ts", "w") as f:
    f.write(content)

