import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Add Module 12 to the very end
module_12 = """
  '12': {
    id:"12", code:"MODULE_12_CUCKING", title:"THE CUCKING", sub:"( The Public Display Asymmetry )",
    labels:["ONE_WAY_DISPLAY","TITLE_WITHOUT_DUTIES","PUBLIC_HUMILIATION"],
    objective:"To hold the title of partner in private while performing singlehood in public: maximum display-labor extracted from the victim — duet joins, art, gifts, profile real estate — against zero visible reciprocity. The audience sees a woman devoted to a man who does not appear to know she exists. (Evidence status: testimony + StarMaker record; the join arithmetic is the Operative's own count on the platform.)",
    epigraphs:[
      { who:"Merry", src:"TESTIMONY", text:"I joined over like 50 of his damn duets. I joined one of his duets like every day — to his two he ever joined me, one on camera. And he, before me, he joined people fine. And after me, apparently he joined people fine too." },
      { who:"Merry", src:"TESTIMONY", text:"Bitch, you never sang a fucking duet with me after the first one. What the fuck do you mean you're my duet partner?" }
    ],
    mechanismTitle:"<b>I.</b> THE MECHANISM — THE ONE-WAY STAGE",
    mechanism:[
      {title:"Sell the title", text:"The duet partnership is made a big deal of. A title creates duties of display — so she begins performing the bond publicly, where everyone can see it."},
      {title:"Extract the performance", text:"Daily duet joins. Art of the two of them. Gifts. A profile plastered with his name. All of it public, and some of it paid for in actual money."},
      {title:"Return nothing visible", text:"Two joins back, ever — one on camera. His profile: Jay in the spots, no mention of Merry. Before her he joined people fine; after her, apparently fine too. Only during her did joining people become impossible."},
      {title:"Let the audience finish it", text:"The asymmetry needs no narration. Anyone clicking from her profile to his could see the entire shape of it. The humiliation runs itself."}
    ],
    loop:"⟲ <b>THE AUDIENCE DOES THE WORK</b> — THE HUMILIATION RUNS ITSELF",
    exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
    exhibits:[
      { num:"12.1", status:"ASYMMETRY_ARITHMETIC",
        name:"The Join Ledger",
        ids:[["TESTIMONY"],["STARMAKER"]],
        note:"She counted: 50+ of his duets joined — roughly one a day — against two of hers, one on camera. Izzy: joined 16 times. Other girls: joined repeatedly, before her and after her.",
        analysis:"The capability was never in question — only the allocation. The same machinery as the camera “complex”: not a condition, a sanction. He could join people. He simply did not join her — and the joins were public, so the ledger was too.",
        crossref:["02","MODULE_02 — THE WITHHOLDING"] },
      { num:"12.2", status:"ONE_WAY_DISPLAY",
        name:"The Billboard",
        ids:[["TESTIMONY"],["STARMAKER"]],
        note:"Her profile: Derek, Derek, Derek, Derek, Derek, Derek. Click his little picture on her profile and it delivers you to his — where Jay holds the spot and there is no mention of Merry at all.",
        analysis:"Her profile advertised him; his profile erased her. The pipeline ran one direction only: her audience, delivered to him — his audience, never shown she exists. This is the erasure's public face, worn for months while the relationship was still supposedly alive.",
        crossref:["07","MODULE_07 — THE ERASURE"] },
      { num:"12.3", status:"UNPAID_PRODUCTION",
        name:"The Art Economy",
        ids:[["TESTIMONY"]],
        note:"More than half a year of making art: art of them, art for him, gifts for him. The AI art cost money — her money.",
        analysis:"The extraction had a literal invoice. She was not only performing the partnership publicly; she was funding its set design, for an audience he was simultaneously telling nothing. See MODULE_06 for the full economy; this exhibit is about its visibility.",
        crossref:["06","MODULE_06 — THE EXPLOITATION"] },
      { num:"12.4", status:"TITLE_RETENTION",
        name:"“But I'm Your Duet Partner”",
        ids:[["TESTIMONY"]],
        note:"Months in, as she is already letting go of the relationship, he re-invokes the title: but I'm your duet partner. A title he never once performed after the first duet.",
        analysis:"He never performed the partnership — but he never released the title either, because the title was the pump. As long as she believed she held it, the joins, the art, the gifts, and the public display kept flowing. Retaining the name while declining the duties is not a relationship status; it is a billing arrangement.",
        crossref:["01","MODULE_01 — THE PROMISES"] },
      { num:"12.5", status:"SHAME_REASSIGNED",
        name:"The Audience Verdict",
        ids:[["TESTIMONY"]],
        note:"“I know people were looking at me laughing. He made me look stupid to people.” — and then the reframe: “If I were the type to get embarrassed, I would be. Luckily, I'm really not. He should be embarrassed for doing that to me.”",
        analysis:"The humiliation was the public's view of the asymmetry — nothing more, nothing less. She declines the embarrassment. The record agrees with her: the shame belongs to the man who built the one-way stage on purpose, and this module is where it is filed." }
    ],
    impact:[
      "<strong>Sunk-cost spectacle.</strong> Public display raises the price of walking away. Leaving no longer means just losing him — it means admitting, in front of the audience, that the devotion they watched was never returned.",
      "<strong>The title trap.</strong> A partnership that exists only as a title extracts like a job and protects like nothing. She performed the duties of a duet partner for a year and held none of the rights of one.",
      "<strong>Shame, reassigned.</strong> She looked stupid to people because she believed a man's word in public. The record now shows the word, the man, and the arithmetic — and the embarrassment has been refiled under his name."
    ],
    gallery:{ title:"<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE · CLICK TO ENLARGE",
      images:[
        { src:"https://storage.googleapis.com/astraltrash_other/derek/cuck1.png", cap:"<b>HER AI SESSION</b> — “I am hidden while she is protected and prioritized.”" },
        { src:"https://storage.googleapis.com/astraltrash_other/derek/cuck2.png", cap:"“Derek Derek Derek all over my profile. That's not just anger. That's shame mixed with grief.”" },
        { src:"https://storage.googleapis.com/astraltrash_other/derek/art1112.jpeg", cap:"<b>THE ART</b> — DEREK/MERRY, glitch piece. Made for two. Displayed by one." }
      ]},
    addendum: [
      { title: "THE NUMBERS", text: "How he made such a cuck of me. C-U-C-K. A cuck. Hey, this pretty boy got me, a girl, so excited by promising me the duet partner I'd always wanted. I gushed to so many people and bragged, and I spent half a year, at least half of that year, more than half a year, making art of us, art for him, gifts for him, art for his fucking shit. That shit cost money for me, by the way. The AI art stuff, that cost money.\\n\\nAnd I joined over like 50 of his damn duets. I joined one of his duets like every day — to his two he ever joined me, one on camera. And he, before me, he joined people fine. And after me, apparently he joined people fine too. But when he was promising me, and I was doing all this art for us, and I had Derek, Derek, Derek, Derek, Derek, Derek all over my profile.\\n\\nAt one point, I did a thing and I looked to see how many, like, like what the numbers were. Like he had joined Izzy like 16 times, which he'd done her for fucking ever, sure, whatever. Like he had joined all these other girls all these times, and he'd joined me twice. And I was supposed to be his fucking duet partner. He made a big deal out of that duet partnership." },
      { title: "DEREK DEREK DEREK", text: "Everything was Derek, Derek, Derek, Derek, Derek, Derek. When you clicked on Derek's little picture on my profile, it took me to his profile, where it was Jay up there, and no mention of me. He hadn't joined me." },
      { title: '"BUT I\'M YOUR DUET PARTNER"', text: "At one point, there after like months and months, like before I was already letting go of the relationship at this point. This was just a few months ago. He was like, but I'm your duet partner. Bitch, you never sang a fucking duet with me after the first one. What the fuck do you mean you're my duet partner? No the fuck you're not. You let me think you were, you let me act like you were for a long fucking time before I figured out that you weren't. You made a cuck of me." },
      { title: "THE AUDIENCE", text: "I feel silly. If I were the type to get embarrassed, I would be. Luckily, I'm really not. Luckily, I'm like, he should be embarrassed for doing that to me. But at the same time, I know people were looking at me laughing. Like I looked, he made me look stupid to people. And fine, whatever fucking. But he did, and that was not cool. He made such a huge cuck of me. *Fuck him.*" }
    ],
    yaml:`module: MODULE_12_CUCKING
behavioral_labels: [ONE_WAY_DISPLAY, TITLE_WITHOUT_DUTIES, PUBLIC_HUMILIATION]
evidence_points:
  - { event: "Join ledger — 50+ of his vs. 2 of hers (1 on camera); Izzy 16",
      source: user_testimony, platform: starmaker, status: ASYMMETRY_ARITHMETIC }
  - { event: "Profile billboard — Derek all over hers; no mention of her on his",
      source: user_testimony, platform: starmaker, status: ONE_WAY_DISPLAY }
  - { event: "Art economy — half a year of art and gifts, paid for by her",
      source: user_testimony, status: UNPAID_PRODUCTION }
  - { event: "'But I'm your duet partner' — title retained, duties declined",
      source: user_testimony, status: TITLE_RETENTION }
  - { event: "Public humiliation — audience could see the asymmetry",
      source: user_testimony, status: SHAME_REASSIGNED }
impact_metric:
  victim_state: "Publicly displayed devotion, privately unacknowledged"
  perpetrator_gain: "Her audience, her art, her labor — at zero visible cost"`,
    prev:["11","MODULE 11 — THE GHOST ANALYSIS"],
    next:null
  }
};
"""

content = re.sub(r'};\n*$', module_12, content)
content = content.replace('next:null', 'next:["12","MODULE 12 — THE CUCKING"]')

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("done pt4")
