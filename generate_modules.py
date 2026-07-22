import json

def get_module(num, content):
    return f"  '{num}': {{\n    {content}\n  }}"

m01 = """id:"01", code:"MODULE_01_PROMISES", title:"THE PROMISES", sub:"( The Hook & The Bait )",
  labels:["LOVE_BOMBING","FUTURE_FAKING"],
  objective:"The establishment of an emotional contract designed to secure maximum investment from the victim while providing zero tangible commitment from the perpetrator. (Pre-log era: user testimony + StarMaker profile + third-party reports; log-era receipts cross-referenced in MODULE_03.)",
  epigraphs:[
    { who:"Merry", src:"WA-1851", text:"I wasn\\u2019t the one that put the idea in MY head. That was you. I was fine. I didn\\u2019t have a duet partner never had never would as far as I was concerned before you came up to me and offered yourself to be the thing I\\u2019d ALWAYS WANTED so bad on a silver fucking platter" },
    { who:"Derek", src:"WA-0605", text:"When you can make, or even just display, one single consideration in an outward direction \\u2014 then I will continue to make sure someone is placing considerations into this pre-existing complex\\u2026" }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE BLUEPRINT OF THE SCAM",
  mechanism:[
    {title:"Find the void", text:"An eight-year aspiration for a creative and emotional anchor is identified. Derek positions himself as the sole provider of its fulfillment."},
    {title:"Offer a status, not a collaboration", text:"The 'Dedicated Duet Partner' title creates an 'unofficially official' bond that feels exclusive and special — classic future-faking. Defenses drop; investment and tolerance rise."},
    {title:"Stack the secondary hooks", text:"Once the primary hook is set, he adds the promise of video calls (visual intimacy) and a shared living situation (physical stability)."},
    {title:"Promises become payments", text:"Each promise functions as a 'payment' for Merry's continued patience and tolerance of his increasingly erratic behavior."}
  ],
  loop:"⟲ <b>EVERY PROMISE BUYS MORE PATIENCE</b> — YOU CANNOT PULL A RUG THAT WAS NEVER LAID. HE LAID IT.",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"1.1", status:"FRAUDULENT",
      name:"The \\u201CDedicated Duet Partner\\u201D Contract",
      ids:[["TESTIMONY"],["STARMAKER"],["DOSSIER §1"]],
      note:"Derek asked Merry to be his dedicated duet partner, framed as a mutual commitment to sing together and build a friendship. He performed exactly one (1) duet — \\u201CThe Bedrock Anthem\\u201D — then ceased all collaborative effort for an entire year.",
      analysis:"By granting one single \\u201Cwin\\u201D early on, he proved the promise was possible, making a year of silence read as a \\u201Ctemporary hurdle.\\u201D This manufactured the Sunk Cost Fallacy: she stayed because she had already invested so much in the idea of the partnership." },
    { num:"1.2", status:"MANIPULATED",
      name:"The \\u201CTwo-Week\\u201D Video Call Timeline",
      ids:[["TESTIMONY"],["WA-0560"],["WA-0605"]],
      note:"Derek explicitly stated that within \\u201Ca couple of weeks\\u201D they would have a face-to-face video call. The couple of weeks became months, then became a \\u201Crule\\u201D where the date was pushed back indefinitely — corroborated in-log by WA-0560 and WA-0605.",
      analysis:"The carrot on a stick. A specific but fake timeline keeps the victim in anticipatory anxiety. The promise was never intended to be kept; it was intended to be negotiated. This is the origin of the goalpost system.",
      crossref:["module03.html","MODULE_03 — THE RUG-PULLS"] },
    { num:"1.3", status:"FANTASY_CONTROL",
      name:"The \\u201CMove-In\\u201D Fantasy",
      ids:[["TESTIMONY"]],
      note:"Discussions occurred regarding Merry moving to Atlantic City to live with Derek. No concrete plans were ever finalized, and Derek remained unhoused and unstable throughout.",
      analysis:"High-stakes future-faking. Suggesting a shared household escalated the perceived seriousness of the relationship, ensuring she felt a level of commitment that justified providing extreme emotional support and unearned patience." }
  ],
  impact:[
    "<strong>The Dopamine Loop.</strong> Every mention of the \\u201Cfuture\\u201D (the duet, the call, the move) triggered a dopamine release; every withholding created withdrawal. The cycle is identical to the mechanics of gambling addiction.",
    "<strong>The Erasure of Self.</strong> Because the \\u201Cpartnership\\u201D was the center of the relationship, Merry began to define her value by her ability to \\u201Cearn\\u201D the duet or the call. She transitioned from a creator to a supplicant.",
    "<strong>The Setup for the Rug-Pull.</strong> You cannot pull a rug if there is no rug. By promising the duet and the video call, he laid it, waited for her to put all her weight on it — and created the exact conditions MODULE_03 documents."
  ],
  yaml:`module: MODULE_01_PROMISES
behavioral_labels: [LOVE_BOMBING, FUTURE_FAKING, INTERMITTENT_REINFORCEMENT]
evidence_points:
  - { event: "Duet Partnership Agreement", promise: "Dedicated duet partner",
      reality: "One song performed; zero collaboration for 12 months", status: FRAUDULENT }
  - { event: "Video Call Timeline", promise: "Face-to-face within 'a couple of weeks'",
      reality: "Delayed indefinitely; used as punishment tool", status: MANIPULATED,
      log_corroboration: [WA-0560, WA-0605] }
  - { event: "Relocation Proposal", promise: "Merry moving to Atlantic City",
      reality: "Derek remained unhoused; no viable plan ever existed", status: FANTASY_CONTROL }
impact_metric:
  victim_state: "Hyper-investment / Anticipatory Anxiety"
  perpetrator_gain: "Maximum emotional labor at zero cost"`,
  prev:null,
  next:["module02.html","MODULE 02 — THE WITHHOLDING"]"""

m02 = """id:"02", code:"MODULE_02_WITHHOLDING", title:"THE WITHHOLDING", sub:"( The Control Mechanism )",
  labels:["SENSORY_DEPRIVATION","COERCIVE_CONTROL","EMOTIONAL_STARVATION"],
  objective:"To maintain a power imbalance by identifying the victim's primary communication needs and systematically denying them, thereby forcing her into a state of dependency and desperation.",
  epigraphs:[
    { who:"Derek", src:"WA-1688", text:"The Whatsapp thing is just too much when I'm overwhelmed..... and the video message thing is just \\uD83D\\uDE48\\uD83D\\uDD2B\\n\\nWe all have our complexes, Merry" },
    { who:"Merry", src:"WA-0455", text:"I can not communicate fully - I cannot trust u fully - I cannot fully feel part of this thing if you NEVER LET ME SEE YOU. \\u2026 I AM MISSING OUT on 98% of the information in your messages to me simply bc I cannot read your micro expressions and body language \\u2026 to me it is literally like being completely in the dark" }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE ARCHITECTURE OF ABSENCE",
  mechanism:[
    {title:"Map the sensory requirements", text:"For a neurodivergent person, visual cues — microexpressions, lip-reading, body language — are not bonuses. They are essential data for processing human interaction."},
    {title:"Restrict the channel", text:"Communication is confined to audio-only, muffled, thick-accented calls — effectively blindfolding her social intuition and forcing total reliance on his verbal framing of reality."},
    {title:"The 'complex' cover story", text:"The refusal is framed as a psychological struggle, transforming an act of control into a request for sympathy — and her needs into a test of her patience."},
    {title:"Rations", text:"Occasional old photos provide just enough reward to keep the dopamine loop alive and prevent her from giving up entirely."}
  ],
  loop:"⟲ <b>STARVATION BY DESIGN</b> — ABSENCE AS ARCHITECTURE",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"2.1", status:"SABOTAGE",
      name:"The Auditory Processing Blockade",
      ids:[["TESTIMONY"],["WA-1688"],["WA-0790"]],
      quote:"the video message thing is just 🙈🔫",
      note:"Merry requires visual input to overcome auditory processing issues and a thick New Jersey accent. Derek refused video calls, bubbles, or any visual accompaniment — allowing her to spend 40% of their hours-long conversations saying \\u201CHuh? What? Say that again\\u201D without offering the simplest solution.",
      analysis:"Cognitive sabotage. Constant low-grade confusion is a prime state for manipulation: he limited the data she could receive to make her dependent on his interpretation of it." },
    { num:"2.2", status:"FRAUDULENT_VULNERABILITY",
      name:"The \\u201CComplex\\u201D as a Shield",
      ids:[["TESTIMONY"],["STARMAKER"],["WA-1135","12/29/25"],["WA-1494","01/22/26"]],
      quote:"Video call, 1 hr  —  system record WA-1135\\nVideo call, 55 min —  system record WA-1494",
      note:"He claimed a \\u201Ccomplex\\u201D made camera performance impossible. He was visible on camera in old StarMaker videos, later performed duets with other women — and held two long video calls with Merry, one just seventeen days after declaring a video call would \\u201Cnever happen between us.\\u201D",
      analysis:"Fraudulent vulnerability: a fake weakness used to exert real power. The \\u201Ccomplex\\u201D was situational — it existed only when it served as an excuse to deny her, and it made the conversation about his trauma rather than her needs.",
      crossref:["module03.html#ex3.6","MODULE_03 — THE CAPABILITY RECEIPTS"] },
    { num:"2.3", status:"BREADCRUMBING",
      name:"The \\u201CRations\\u201D System",
      ids:[["TESTIMONY"]],
      note:"Derek would occasionally send old photos of himself, which Merry jokingly referred to as \\u201Crations.\\u201D",
      analysis:"Intermittent reinforcement. Small, controlled glimpses of his face — the \\u201Ccrumbs\\u201D of affection — make the starvation feel like a challenge rather than abuse. It mirrors captor/addict dynamics exactly." }
  ],
  impact:[
    "<strong>Sensory Frustration & Exhaustion.</strong> Hours of decoding a muffled voice without visual cues leads to sensory overload and cognitive fatigue — leaving her too exhausted to challenge his narratives or notice red flags.",
    "<strong>The \\u201CSavior\\u201D Paradox.</strong> Because Derek was the only one providing the \\u201Cmorning calls\\u201D and \\u201Cemotional support,\\u201D she felt she had to accept the withholding as the price of the safety he provided.",
    "<strong>The Power of the Invisible.</strong> By remaining a voice rather than a person, he could be whoever he wanted to be in her head. A video call would have brought him into the realm of human fallibility — and accountability."
  ],
  yaml:`module: MODULE_02_WITHHOLDING
behavioral_labels: [SENSORY_DEPRIVATION, COERCIVE_CONTROL, INTERMITTENT_REINFORCEMENT]
evidence_points:
  - { event: "Visual Communication Denial", need: "Lip-reading/microexpressions",
      action: "Consistent refusal of video", status: SABOTAGE,
      log_corroboration: [WA-1688, WA-0790] }
  - { event: "The 'Complex' Narrative", claim: "Unable to be on camera",
      contradiction: "Videos with others; duets with other women; WA-1135 (1hr); WA-1494 (55min)",
      status: FRAUDULENT_VULNERABILITY }
  - { event: "The Rations System", action: "Occasional old photos",
      result: "Hope maintained via intermittent reward", status: BREADCRUMBING }
impact_metric:
  victim_state: "Sensory Exhaustion / Cognitive Dependence"
  perpetrator_gain: "Total control of information and image"`,
  prev:["module01.html","MODULE 01 — THE PROMISES"],
  next:["module03.html","MODULE 03 — THE RUG-PULLS"]"""

m03 = """id:"03", code:"MODULE_03_RUG_PULLS", title:"THE RUG-PULLS", sub:"( The Neurological Trigger )",
  labels:["GOALPOST_MOVING","INTERMITTENT_REINFORCEMENT","PUNITIVE_RESET"],
  objective:"To convert every concrete promise into a moving target, so that fulfillment is always one apology, one behavior-fix, one \\u201Cright feeling\\u201D away — and to weaponize the resulting destabilization (especially against a neurodivergent need for predictability) as proof that the victim is \\u201Ctoo much.\\u201D",
  epigraphs:[
    { who:"Derek", src:"WA-0560", text:"It will happen when it doesn't feel like this.     Period" },
    { who:"Derek", src:"WA-0605", text:"\\u2026then I will PROMISE just as readily, that a video call will never happen between us, to protect my progress _from_ you." },
    { who:"Merry", src:"WA-0736", text:"You just dangle the carrot in front of my face, knowing good well you\\u2019re never gonna give me the fucking carrot fuck off with your fucking carrot." }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — FOUR MOVING PARTS, ONE LOOP",
  mechanism:[
    {title:"Offer unprompted", text:"Derek himself raises the video call, unprompted — establishing that he controls the promise's existence."},
    {title:"Attach a condition", text:"When the promise comes due, a new requirement materializes that was never part of the original agreement."},
    {title:"Punitive reset", text:"When Merry protests the moved goalpost, the protest itself becomes the new reason for delay. Time owed resets to zero. Or to infinity."},
    {title:"Reframe the meltdown", text:"The distress produced by steps 1–3 is quoted back as evidence of why she can't have the thing. The reaction to the abuse becomes the justification for the abuse."}
  ],
  loop:"⟲ <b>AND THE LOOP RESTARTS</b> — A RUG-PULL IS NOT AN EVENT, IT IS A SYSTEM",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"3.1", status:"BAIT",
      name:"The Unprompted Offer",
      ids:[["WA-0241","12/08/25 2:55 PM"]],
      quote:"Video call late tonight?",
      note:"After a 28-day disappearance (Nov 6 → Dec 5), Derek resurfaces, does multiple voice calls across Dec 6–8, and then — unprompted — dangles a video call that same night. No record of it occurring. The offer functioned as a re-entry gift: instant re-escalation of intimacy at zero cost to him.",
      analysis:"The offer is the reward. It was never an appointment; it was a dopamine token to reboot her investment after a month of silence." },
    { num:"3.2", status:"GOALPOST_DISSOLVED",
      name:"The Condition Appears",
      ids:[["WA-0560","12/12/25 9:09 AM"],["SC-28","the hand-circled page"]],
      quote:"It will happen when it doesn't feel like this.  Period",
      note:"Morning of the Dec 12 confrontation. Merry, after ~11 months of waiting, states the promise is due. Derek's response converts a year-old commitment into a behavioral contingency: the call happens when the vibe is right — a condition that is unmeasurable, unverifiable, and defined entirely by him.",
      analysis:"This is the goalpost literally dissolving. There is no date to miss when the date is \\u201Cwhen I feel like it.\\u201D She circled this exchange in the screenshot dossier because it is the whole system in one line." },
    { num:"3.3", status:"PROMISE_LAUNDERING",
      name:"The \\u201CConsideration\\u201D Speech — the promise becomes a wage (and then a confession)",
      ids:[["WA-0605","12/12/25 9:23 AM"]],
      quote:"When you can make, / or even just display, / one single consideration / in an outward direction / then I will continue to make sure someone is placing considerations into this pre-existing complex [...] I will PROMISE just as readily, that a video call will never happen between us, to protect my progress from you.",
      note:"Fourteen minutes after WA-0560, Derek formalizes the contingency into a contract of emotional labor: display consideration → earn a promise. But the full sentence is worse than a wage. Buried mid-clause he states the actual endgame — her need is, in his own words, the thing his \\u201Cprogress\\u201D must be protected from.",
      analysis:"Promise-laundering with a confession inside. The original debt is written off and replaced with a new currency in which she must now earn his willingness to re-promise — while the sentence itself quietly converts \\u201Cnot yet\\u201D into \\u201Cnever.\\u201D The arrears vanish; the ledger resets with her in the red; and the goalpost was never on the field at all." },
    { num:"3.4", status:"TRIANGULATION_THREAT",
      name:"The Replacement Threat",
      ids:[["WA-0654","12/12/25 9:36 AM"]],
      quote:"I'll tell you what.....I'll find a FRIEND who will help me work on my complexes, not make them worse. Then once I'm comfortable on camera, I'll come back & chat & sing & be well-adjusted & happy",
      analysis:"The rug-pull now has teeth. Not only is the promise withdrawn — it will be fulfilled with someone else first, and she will watch. (He follows through on exactly this: see MODULE_07, the duets with other women.) The threat converts her protest into a competition she can lose.",
      crossref:["module07.html","MODULE_07 — THE ERASURE"] },
    { num:"3.5", status:"PUNITIVE_RESET",
      name:"The Punitive Freeze — 8 days of silence after the confrontation",
      ids:[["WA-0958","emoji wall"],["WA-0995–0996","double missed calls"],["WA-1018","12/24"]],
      note:"After the Dec 12 confrontation, Derek goes silent for 8 days, then resurfaces Dec 20–23 with emoji walls and double missed calls — no acknowledgment of the confrontation, the promise, or the freeze. On Dec 24: \\u201COr a dropped call...\\u201D",
      analysis:"The punitive reset executed in calendar form. The confrontation cost her 8 days; its resolution cost him nothing — he re-enters as if continuity were never broken. The emoji wall is a presence-token: minimum viable contact, maximum plausible deniability." },
    { num:"3.6", status:"CAPABILITY_RECEIPT",
      name:"The Capability Receipts — TWO video calls after a year of \\u201Cthe complex\\u201D",
      ids:[["WA-1135","12/29/25 9:53 PM"],["WA-1494","01/22/26 1:17 AM"],["WA-1496","voice, 7 min"],["WA-1499","voice, 39 min"]],
      quote:"Video call, 1 hr  —  system record WA-1135\\nVideo call, 55 min —  system record WA-1494",
      note:"After a full year in which a video call was structurally impossible due to \\u201Cthe complex\\u201D — and just 17 days after the Dec 12 speeches in which the call would only happen \\u201Cwhen it doesn't feel like this\\u201D (WA-0560) and would in fact \\u201Cnever happen between us\\u201D (WA-0605) — Derek gets on a one-hour video call. Then, mid-January-thaw, a second one at 1 AM.",
      analysis:"The single most corrosive fact for the \\u201Ccomplex\\u201D narrative — twice over. The barrier was never capability; it was leverage. The calls happened when they cost him nothing and bought maximum goodwill — and could be withheld again the moment each thaw ended. Which they were." },
    { num:"3.7", status:"GOALPOST_REMOVED_FROM_FIELD",
      name:"The Final Dissolution — withdrawal as \\u201Cdelivering my conquered complex\\u201D",
      ids:[["WA-1906","02/16/26 2:31 AM"]],
      quote:"So I end up choosing to withdraw / In other to — / 1.) Not be a facilitator, enabler, conduit of unrighteous unnecessary negativity / 2.) To have a better chance at repairing the breech of trust, by delivering to you, my conquered complex.",
      analysis:"The end-state of the system: disappearance rebranded as progress on the promise itself. He is not ghosting her — he is \\u201Cworking on the complex,\\u201D offstage, indefinitely, and any objection is \\u201Cunrighteous unnecessary negativity.\\u201D The goalpost has left the field entirely." }
  ],
  impact:[
    "<strong>Manufactured instability.</strong> Each cycle (offer → condition → reset → reframe) teaches the nervous system that stated plans are fiction. For a neurodivergent person this is not metaphorically destabilizing — it is a direct attack on the mechanism used to regulate.",
    "<strong>The meltdown as product.</strong> The Dec 12 logs (SC-01–28) show the output: hours of escalating distress from Merry, met with calm, formatted, sermon-like paragraphs from Derek. The asymmetry is then harvested — her volume becomes his evidence.",
    "<strong>The debt that can never be called in.</strong> By Feb 2026 the promise has been so thoroughly laundered (offer → condition → wage → threat → freeze → offstage \\u201Cconquering\\u201D) that any demand for fulfillment sounds, in his framing, like cruelty toward a man \\u201Cworking on himself.\\u201D"
  ],
  yaml:`module: MODULE_03_RUG_PULLS
behavioral_labels: [GOALPOST_MOVING, INTERMITTENT_REINFORCEMENT, PUNITIVE_RESET]
evidence_points:
  - { event: "Unprompted offer after 28-day silence", evidence: [WA-0241], status: BAIT }
  - { event: "Promise converted to behavioral contingency", evidence: [WA-0560, SC-28], status: GOALPOST_DISSOLVED }
  - { event: "Consideration speech — promise becomes a wage", evidence: [WA-0605], status: PROMISE_LAUNDERING }
  - { event: "Replacement threat", evidence: [WA-0654], status: TRIANGULATION_THREAT, cross_ref: MODULE_07 }
  - { event: "Punitive freeze, 8 days", evidence: [WA-0958, WA-0995, WA-0996, WA-1018], status: PUNITIVE_RESET }
  - { event: "1hr video call 17 days after 'never happen'", evidence: [WA-1135], status: CAPABILITY_RECEIPT }
  - { event: "55min video call, second falsification", evidence: [WA-1494, WA-1496, WA-1499], status: CAPABILITY_RECEIPT }
  - { event: "Withdrawal rebranded as progress", evidence: [WA-1906], status: GOALPOST_REMOVED_FROM_FIELD }
impact_metric:
  victim_state: "Manufactured instability / meltdown cycles harvested as evidence against her"
  perpetrator_gain: "A promise that can never be called due, and a permanent excuse for its non-fulfillment"`,
  prev:["module02.html","MODULE 02 — THE WITHHOLDING"],
  next:["module04.html","MODULE 04 — THE GASLIGHTING"]"""

m04 = """id:"04", code:"MODULE_04_GASLIGHTING_DARVO", title:"THE GASLIGHTING", sub:"( The Reality Rewrite — DARVO: Deny, Attack, Reverse Victim & Offender )",
  labels:["GASLIGHTING","DARVO","TONE_POLICING","REALITY_REWRITE"],
  objective:"To make the victim's perception the problem. Every injury she names is converted into evidence of her defect — her tone, her \\u201Cperspective,\\u201D her cruelty, her instability — until she is defending her sanity instead of his record. The Feb 16, 2026 session (2:17–3:52 AM) is the machine running at full power.",
  epigraphs:[
    { who:"Derek", src:"WA-1903", text:"You just lack some perspective on things\\n\\nI know it sucks, but I HAVE to be the perspective guy.\\n\\nAnd I can't allow you to say things that you shouldn't hear yourself saying out loud!" },
    { who:"Derek", src:"WA-1924", text:"Because you really shouldn't be capable of thinking what you're thinking    -  but you really shouldn't be capable of saying what you're saying still.\\n\\nAnd that concerns me about my friend more than anything else\\n\\nLove you  \\uD83D\\uDE18" }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE REWRITE MACHINE",
  mechanism:[
    {title:"Bait the reaction", text:"Withhold, disappear, move the goalpost (Modules 2–3) until the victim — autistic, sleep-deprived from phone labor, a year into broken promises — reacts with volume."},
    {title:"Discard the substance, indict the style", text:"Her content (\\u201Cyou broke a year of promises\\u201D) is never answered. Her delivery (\\u201Cyou said fuck you\\u201D) becomes the entire trial."},
    {title:"Crown himself the injured party", text:"He is the one with complexes, traumas, overwhelm; she is the \\u201Cfacilitator of unrighteous negativity.\\u201D Offender and victim swap seats — in writing, calmly, with bullet points."}
  ],
  loop:"⟲ <b>DENY · ATTACK · REVERSE</b> — THE MACHINE RUNS ON HER DISTRESS",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — EVERY STAGE, QUOTED VERBATIM",
  exhibits:[
    { num:"4.1", status:"DENY",
      name:"The disappearance was her accommodation failure",
      ids:[["WA-1688","02/15/26 4:08 PM"],["WA-1684","11 days silent"],["WA-1663–1671","proof-of-life calls"]],
      quote:"The Whatsapp thing is just too much when I'm overwhelmed..... and the video message thing is just 🙈🔫 / We all have our complexes, Merry / Ours just happen to clash sometimes / But I wouldn't even think the words 'fuck you' when they do / Because they are clashing / Not us",
      note:"He has just returned from 11 days of total silence, during which she sent audio messages into the void and made 4-second \\u201Cproof of life\\u201D calls because she was worried he was dead.",
      analysis:"The event under review is an 11-day disappearance. His opening move erases it: the real subject is her \\u201Cfuck you.\\u201D The disappearance becomes weather (\\u201Ccomplexes clashing\\u201D); her fear-response becomes the crime." },
    { num:"4.2", status:"PSEUDO_ACCOUNTABILITY",
      name:"The Past-Tense Confession — \\u201CI'm wrong 100%\\u201D (terms & conditions apply)",
      ids:[["WA-1879","02/16/26 2:17 AM"]],
      quote:"'was' & 'wasn't' ← Those I'm taking full responsibility for. And I would like to remedy those shortcomings (despite the fact that they're directly linked to traumas & complexes, which should be taken into consideration… It's on me / I'm wrong 100%",
      analysis:"It looks like the confession she begged for. Read the grammar. Responsibility is accepted only for the past tense — and immediately discounted by the parenthetical. Technically an admission; functionally a plea bargain." },
    { num:"4.3", status:"DENY",
      name:"\\u201CThe guilt game\\u201D — present and future declared negotiable",
      ids:[["WA-1885","02/16/26 2:24 AM"]],
      quote:"'isn't'  'is'  'will be'  'won't be' / ↑ These are up for grabs ↑ / in the guilt game / I understand what you're saying. I understand your rationality on things. But there's a major piece of the puzzle you're simply not seeing here.",
      analysis:"Seven minutes after \\u201CI'm wrong 100%,\\u201D he carves out everything that is, will be, and won't be — the entire living relationship — as contestable. Then the pivot: she is missing \\u201Ca major piece of the puzzle.\\u201D Her rationality is acknowledged and overruled in the same breath." },
    { num:"4.4", status:"REVERSE_VICTIM_OFFENDER",
      name:"Reverse — her trust was the original sin",
      ids:[["WA-1891","02/16/26 2:27 AM"]],
      quote:"If you compound someone's complex, because you're upset about a breech of trust, that you probably shouldn't have placed on something so delicate.... you end up compounding how upset you are because it's going to be more difficult to repair or reverse that breech.",
      analysis:"The purest DARVO in the archive. He broke trust. She got upset. His verdict: the upset is her fault for having placed trust \\u201Con something so delicate.\\u201D The offender is the man who broke the promise; the offender, in his telling, is the woman who believed it.",
      crossref:["module07.html#ex7.2","MODULE_07 — THE RETROACTIVE RECLASSIFICATION"] },
    { num:"4.5", status:"ATTACK",
      name:"\\u201CThe perspective guy\\u201D — self-appointed editor of her reality",
      ids:[["WA-1903","02/16/26 2:29 AM"],["WA-0366","12/09/25"]],
      quote:"You just lack some perspective on things / I know it sucks, but I HAVE to be the perspective guy. / And I can't allow you to say things that you shouldn't hear yourself saying out loud!",
      analysis:"Three moves in three lines: her perception is deficient; he is the corrective authority; censorship is framed as protection. He is not arguing her facts are wrong — he is asserting jurisdiction over what she may think and say. The perspective defense is a fixed habit, not a one-off." },
    { num:"4.6", status:"REVERSE_VICTIM_OFFENDER",
      name:"The Moral Exit — withdrawal as hygiene",
      ids:[["WA-1906","02/16/26 2:31 AM"]],
      quote:"So I end up choosing to withdraw / In other to — / 1.) Not be a facilitator, enabler, conduit of unrighteous unnecessary negativity / 2.) To have a better chance at repairing the breech of trust, by delivering to you, my conquered complex.",
      analysis:"Having denied, attacked, and reversed, he exits as the virtuous party. Her pain is \\u201Cunrighteous unnecessary negativity\\u201D; his silence is a gift in progress. This is the same withdrawal that lasted until May." },
    { num:"4.7", status:"GASLIGHT_FRAME",
      name:"\\u201CI only set the stage\\u201D — the gaslighter's stage direction",
      ids:[["WA-1975","02/16/26 3:52 AM"]],
      quote:"I only set the stage / Now you go and add to that stage / Or make an appeal to alter what I tried to objectively set up, granted, from my perspective",
      analysis:"The closing frame: his narrative is \\u201Cobjective\\u201D set design; her account is an \\u201Cappeal\\u201D that may be filed for review. The epistemic hierarchy is total — he authors reality, she petitions it." },
    { num:"4.8", status:"LEGACY_GASLIGHT",
      name:"The Post-Log Thesis — \\u201Cshe's mad so she doesn't have to hate herself\\u201D",
      ids:[["TESTIMONY","third-party framing"]],
      note:"Derek's post-breakup claim: Merry's anger is self-deception — she knows he's right and performs rage to avoid self-hatred.",
      analysis:"Rage-avoidance theories are unfalsifiable — that is their function. What is falsifiable is the record: 11-day silences, a year-old promise converted to \\u201Cwhen it doesn't feel like this,\\u201D a confession revoked within seven minutes, and a 55-minute video call proving the impossible was always possible. Her anger has timestamps. His \\u201Crightness\\u201D has none." }
  ],
  impact:[
    "<strong>Reality debt.</strong> Each cycle forces the victim to choose between her memory and the relationship. Choosing the relationship means retro-editing her own perceptions — the core injury of gaslighting.",
    "<strong>The tone tax.</strong> Because only her delivery is ever tried, she must modulate the expression of legitimate grievance until it is palatable to the person who caused it — a second job, performed during injury.",
    "<strong>Confession exhaustion.</strong> \\u201CHe admitted he was wrong\\u201D is not exculpatory: admissions were issued in the past tense, discounted by trauma-clauses, and revoked for the present within seven minutes."
  ],
  yaml:`module: MODULE_04_GASLIGHTING_DARVO
behavioral_labels: [GASLIGHTING, DARVO, TONE_POLICING]
evidence_points:
  - { event: "11-day disappearance reframed as her language problem", evidence: [WA-1684, WA-1688, WA-1663], darvo_stage: DENY }
  - { event: "Past-tense-only confession", evidence: [WA-1879], darvo_stage: PSEUDO_ACCOUNTABILITY }
  - { event: "Present/future 'up for grabs in the guilt game'", evidence: [WA-1885], darvo_stage: DENY }
  - { event: "Her trust blamed for his breach of it", evidence: [WA-1891], darvo_stage: REVERSE_VICTIM_OFFENDER }
  - { event: "Self-appointed reality editor", evidence: [WA-1903, WA-0366], darvo_stage: ATTACK }
  - { event: "Virtuous withdrawal", evidence: [WA-1906], darvo_stage: REVERSE_VICTIM_OFFENDER }
  - { event: "'Objective' authorship claim", evidence: [WA-1975], darvo_stage: GASLIGHT_FRAME }
  - { event: "Post-breakup thesis", source: user_testimony,
      rebuttal: "Her anger has timestamps; his rightness has none", darvo_stage: LEGACY_GASLIGHT }
impact_metric:
  victim_state: "Reality debt / tone tax / confession exhaustion"
  perpetrator_gain: "Permanent victim status; immunity from the present and future tense"`,
  prev:["module03.html","MODULE 03 — THE RUG-PULLS"],
  next:["module05.html","MODULE 05 — THE TRIANGULATION"]"""

m05 = """id:"05", code:"MODULE_05_TRIANGULATION", title:"THE TRIANGULATION", sub:"( The Jay Hierarchy )",
  labels:["TRIANGULATION","HIERARCHY_GAMES","JEALOUSY_INDUCTION"],
  objective:"To keep the victim in a permanent audition for a rank she can never confirm, by maintaining a visible third party above her on the ladder. (Evidence status: primarily testimony and third-party reports — the Jay material lives mostly in the missing first-ten-months era; log receipts cited where they exist.)",
  epigraphs:[
    { who:"Derek", src:"WA-0654", text:"I'll  tell you what.....I'll find a FRIEND who will help me work on my complexes, not make them worse.\\n\\nThen once I'm comfortable on camera, I'll come back & chat & sing & be well-adjusted & happy" },
    { who:"Merry", src:"WA-0765", text:"Good luck finding anyone else any better at helping you with your complexes than me bc you\\u2019re a stubborn motherficker that refuses to do anything anyone else says unless it was your own idea first" }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE LADDER",
  mechanism:[
    {title:"Name the ranks", text:"\\u201CThe Couple Spot\\u201D on top — public, romantic, where duets and visible affection live. \\u201CThe Best Friend Spot\\u201D below — intimate, private, load-bearing. Merry's rank."},
    {title:"Install the third party", text:"Jay occupies (or claims) the couple spot: the woman in the visible position, recipient of the flirtatious energy Merry was told was reserved for her."},
    {title:"Shield the design", text:"Jay is reportedly dying of cancer — making any objection to her priority position an act of monstrous insensitivity. Grievances arrive pre-convicted."},
    {title:"Make each position police the other", text:"Jay gets the public romance; Merry gets told she's the real confidante, the deeper connection. Each woman's position is used to explain why she can't have the other's."}
  ],
  loop:"⟲ <b>A PERMANENT AUDITION</b> — FOR A RANK SHE CAN NEVER CONFIRM",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"5.1", status:"HIERARCHY_MANAGEMENT",
      name:"The Named Ranks",
      ids:[["TESTIMONY"],["FORENSIC_PATTERN_ANALYSIS"]],
      note:"Derek articulated a hierarchy of attachment — \\u201Ccouple spot\\u201D vs. \\u201Cbest friend spot\\u201D — and placed Merry in the lower one while extracting couple-tier labor from her (nightly calls, future-planning, emotional caretaking; see MODULE_06).",
      analysis:"Naming the ranks is the tell. Casual favoritism happens; a titled hierarchy is a management system. It converts jealousy from an emotion into a job description — she now knows exactly which promotion she's working toward, and exactly who holds it." },
    { num:"5.2", status:"GRIEVANCE_IMMUNITY_DEVICE",
      name:"The Cancer Shield",
      ids:[["TESTIMONY"]],
      note:"Jay was described as dying of cancer — making any objection to her priority position an act of monstrous insensitivity.",
      analysis:"The shield does double duty. It excuses Derek's attention to Jay (\\u201Chow could I abandon a dying woman?\\u201D) and pre-convicts Merry (\\u201Cyou'd begrudge a dying woman?\\u201D). Any grievance about the hierarchy becomes proof of her cruelty — the same reversal machinery as MODULE_04, run through a third party." },
    { num:"5.3", status:"EXCLUSIVITY_FRAUD",
      name:"The Flirtation Contrast",
      ids:[["TESTIMONY"],["FORENSIC_PATTERN_ANALYSIS"]],
      note:"Flirtatious messages directed at Jay, while Merry was told the special, exclusive bond was hers alone.",
      analysis:"The exclusivity was the product being sold to Merry — the \\u201Cunofficially official\\u201D bond. The contrast is the invoice: what was framed as reserved for her was circulating elsewhere. Discovery doesn't end the arrangement; it intensifies it, because now she must compete." },
    { num:"5.4", status:"TRIANGULATION_ON_RECORD",
      name:"The Replacement Threat Made Concrete",
      ids:[["WA-0654","12/12/25 9:36 AM"]],
      quote:"I'll find a FRIEND who will help me work on my complexes, not make them worse. Then once I'm comfortable on camera, I'll come back & chat & sing & be well-adjusted & happy",
      analysis:"In the middle of the Dec 12 confrontation, Derek reaches directly for the triangulation lever: your slot is fillable, and the next occupant will get the camera time you bled for. It is the Jay hierarchy re-declared on the record — the promise that replacement is always one \\u201Cfriend\\u201D away. He later fulfills it visibly.",
      crossref:["module07.html","MODULE_07 — THE ERASURE"] }
  ],
  impact:[
    "<strong>Permanent audition.</strong> A titled rank below the top converts attachment into performance review. The victim's question shifts from \\u201Cis this relationship good?\\u201D to \\u201Chow do I get promoted?\\u201D — a question the perpetrator alone grades.",
    "<strong>Split loyalty, split blame.</strong> The cancer shield meant legitimate grievances arrived pre-labeled as cruelty. She learned to swallow hierarchy injuries whole — training for the larger reality-rewrite in MODULE_04.",
    "<strong>Competitive bonding.</strong> Intermittent glimpses of rival affection function as scarcity marketing: the product never changes, but its perceived value spikes every time someone else appears to hold it."
  ],
  yaml:`module: MODULE_05_TRIANGULATION
behavioral_labels: [TRIANGULATION, HIERARCHY_GAMES, JEALOUSY_INDUCTION]
evidence_points:
  - { event: "Named rank structure (couple spot vs. best friend spot)",
      detail: "Merry in lower rank while providing couple-tier labor",
      source: user_testimony, status: HIERARCHY_MANAGEMENT }
  - { event: "The cancer shield",
      detail: "Jay's priority protected by terminal-illness framing",
      source: user_testimony, status: GRIEVANCE_IMMUNITY_DEVICE }
  - { event: "Flirtation contrast",
      detail: "Flirtation at Jay while exclusivity sold to Merry",
      source: user_testimony, status: EXCLUSIVITY_FRAUD }
  - { event: "Replacement threat during Dec 12 confrontation",
      evidence: [WA-0654], status: TRIANGULATION_ON_RECORD,
      cross_ref: [MODULE_03_RUG_PULLS, MODULE_07_ERASURE] }
impact_metric:
  victim_state: "Permanent audition / swallowed grievances / competitive bonding"
  perpetrator_gain: "Two-directional loyalty extraction; grievances neutralized by the shield"`,
  prev:["module04.html","MODULE 04 — THE GASLIGHTING"],
  next:["module06.html","MODULE 06 — THE EXPLOITATION"]"""


m06 = """id:"06", code:"MODULE_06_EXPLOITATION", title:"THE EXPLOITATION", sub:"( Emotional & Domestic Labor )",
  labels:["LABOR_EXTRACTION","ASYMMETRIC_INVESTMENT","SERVICE_RELATIONSHIP"],
  objective:"To run the relationship as a one-way service economy: maximum emotional and domestic output extracted from the victim; minimum — approaching zero — returned. The labor claims from the pre-log era are testimony; the log era supplies the arithmetic.",
  epigraphs:[
    { who:"Merry", src:"WA-0448", text:"\\u2026as many times as we fell asleep together on the phone (something I don\\u2019t do ftr- every phone call was a concession I MADE for YOU bc it\\u2019s the best I could get at the time)\\u2026 if you can\\u2019t after a year feel comfortable enough to talk to me face to face?" },
    { who:"Derek", src:"WA-1091", text:"Can you send me a Starmaker cover that I haven't heard yet?  I wanna hear something.  Unless you need to chat ASAP, in which case call instead" }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE SERVICE ECONOMY",
  mechanism:[
    {title:"Nightly phone labor", text:"Hours on the phone every night, including sleeping on the phone — despite her stated 'caged animal' sensory aversion to telephone calls. She did it anyway. That is not a preference; that is a shift."},
    {title:"Morning wake-up calls", text:"An alarm-clock function performed daily, on his schedule."},
    {title:"Intimacy, freely given", text:"Shared freely — her idea, her initiative. He never asked. He did not complain. Put it that way and no other way. No transaction occurred; a gift is not a line item."},
    {title:"The Alabama housing offer", text:"Actual residency offered — a roof, a state line, a life. The single largest asset class a person can put on a table."}
  ],
  loop:"⟲ RETURNED THE OTHER WAY: <b>ONE DUET, PHOTO \\u201CRATIONS,\\u201D A 55-MINUTE CALL, AND A 63% SILENCE RATE</b>",
  table:{
    title:"<b>II.</b> THE ARITHMETIC — FROM CHAT_INDEX.CSV, NOV 5 2025 – FEB 16 2026",
    head:["METRIC","VALUE"],
    rows:[
      ["Total messages","2,105"],
      ["Sent by Merry","1,726 (82.0%)"],
      ["Sent by Derek","379 (18.0%)"],
      ["Days in main span","104"],
      ["Days Derek sent anything","38"],
      ["Derek's silence rate","~63% of days"],
      ["Longest documented silence","28 days (Nov 6 → Dec 5, 2025)"],
      ["Second longest","11 days (Feb 3 → Feb 15, 2026)"]
    ],
    note:"Read the first rows again in the context of the \\u201Ccomplex\\u201D: the man who found WhatsApp \\u201Cjust too much when I'm overwhelmed\\u201D (WA-1688) was the recipient of <b>4.5×</b> more messages than he sent. The overwhelm was selective. It never once prevented him from <b>receiving</b> the labor."
  },
  exhibitsTitle:"<b>III.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"6.1", status:"ONE_WAY_ACCOMMODATION",
      name:"The Phone Labor",
      ids:[["TESTIMONY"],["WA-0212","1 hr"],["WA-1226","2 hr"],["WA-1419","4 hr"],["WA-1538","2 hr"],["WA-1494–1499","Jan 22 cluster"]],
      note:"Hours-long nightly calls, overnight sleep calls, wake-up calls — performed despite a documented sensory aversion to phone communication.",
      analysis:"The call durations alone refute the framing that contact burdened him. When the contact was audio — the format that served him and strained her — he had unlimited capacity. The burden only ever materialized around the format that served her (video)." },
    { num:"6.2", status:"FREELY_GIVEN",
      name:"The Freely Given",
      ids:[["TESTIMONY"]],
      note:"Intimacy and play offered freely — her idea, her initiative, her choice. He never asked for any of it. He did not complain. Put it that way and no other way.",
      analysis:"Corrected here as a matter of record: nothing about this was transactional, and none of it is charged to him. The only regret attached to it is hers, and it belongs to the promises — she would have spent that playfulness elsewhere had she known none of them were real. That loss lives in MODULE_01, not in him.",
      crossref:["module01.html","MODULE_01 — THE PROMISES"] },
    { num:"6.3", status:"RESCUE_DIRECTION_REVERSAL",
      name:"The Alabama Offer",
      ids:[["TESTIMONY"]],
      note:"Actual housing — Merry offered Derek a place to live in Alabama while he was unhoused and unstable.",
      analysis:"Note the direction of rescue. The relationship's mythology cast Derek as the provider of stability. In material reality, the only concrete housing offer ever made in this relationship ran from the victim to the perpetrator — and even that was not honored with follow-through." },
    { num:"6.4", status:"EXTRACTION_REFLEX",
      name:"The Reunion Extraction Attempt",
      ids:[["WA-1987–2032","05/16/26"],["WA-2063","24-hr deadline"],["WA-2094","expired"]],
      quote:"First of all — You look great 💯 Like.......you look really healthy.\\nThat 13 second clip will become a feature-length video if i play it enough times. 😅",
      note:"After three months of silence, Merry reopens the channel. Derek's entire substantive engagement: a compliment on her body and confirmation he is replaying her video content. No acknowledgment of the rupture, no apology, no answers.",
      analysis:"The extraction reflex survives even the relationship: immediate re-consumption of her image and attention. When she issues a 24-hour deadline for an actual response (WA-2063), he lets it expire (WA-2094)." }
  ],
  impact:[
    "<strong>Caregiver capture.</strong> Performing daily service functions (alarm clock, overnight presence, emotional regulator) rewires attachment into obligation. Leaving starts to feel like abandoning a dependent — which is precisely the trap.",
    "<strong>Investment escalation.</strong> Every unpaid labor shift raises the sunk cost, raising the required eventual payoff, raising the willingness to tolerate further non-payment. The economy is self-sealing.",
    "<strong>The asymmetry becomes invisible.</strong> Because the labor was framed as love, its scale only becomes visible in aggregate — which is why this module is built from arithmetic rather than anecdote."
  ],
  yaml:`module: MODULE_06_EXPLOITATION
behavioral_labels: [LABOR_EXTRACTION, ASYMMETRIC_INVESTMENT, SERVICE_RELATIONSHIP]
evidence_points:
  - { event: "Nightly/overnight phone labor despite sensory aversion",
      source: user_testimony, log_corroboration: [WA-0212, WA-1226, WA-1419, WA-1538],
      status: ONE_WAY_ACCOMMODATION }
  - { event: "Message asymmetry 4.5:1 (1726 vs 379); Derek silent 63% of days",
      source: chat_index_csv, status: ASYMMETRY_ARITHMETIC }
  - { event: "28-day and 11-day in-log disappearances", source: chat_index_csv, status: WITHDRAWAL_PATTERN }
  - { event: "Intimacy freely given — never requested, never owed",
      source: user_testimony, status: FREELY_GIVEN,
      note: "He did not complain. Put it that way and no other way." }
  - { event: "Alabama housing offer (victim → perpetrator)", source: user_testimony,
      status: RESCUE_DIRECTION_REVERSAL }
  - { event: "Reunion re-consumption without repair",
      evidence: [WA-1987, WA-2032, WA-2063, WA-2094], status: EXTRACTION_REFLEX }
impact_metric:
  victim_state: "Caregiver capture / escalating sunk cost"
  perpetrator_gain: "Full-service support at ~2% performance rate (per Forensic Audit Dossier scoreboard)"`,
  prev:["module05.html","MODULE 05 — THE TRIANGULATION"],
  next:["module07.html","MODULE 07 — THE ERASURE"]"""


m07 = """id:"07", code:"MODULE_07_ERASURE", title:"THE ERASURE", sub:"( The Final Betrayal )",
  labels:["REPLACEMENT_DISPLAY","PUBLIC_REWRITE","LEGACY_MANAGEMENT"],
  objective:"To replace the victim publicly, retroactively reclassify the relationship, and install a final narrative in which the perpetrator is the wronged party and the victim is \\u201Cthe hater.\\u201D The perpetrator has a year of debts on the books and a witness who kept receipts. There are only two solutions — pay, or discredit the ledger.",
  epigraphs:[
    { who:"Derek", src:"WA-1988", text:"Give me a little while to gather my thoughts.    I'll respond ASAP." },
    { who:"Merry", src:"WA-2062", text:"\\u2026the longer I wait on u here for u to say the thing the more I just want to hit block again and forget about it. It seemed like a good idea at the time but I\\u2019m feeling all those awful feelings u made me feel that made me go away originally and wondering why I did this" }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — DELETE AND REPLACE",
  mechanism:[
    {title:"Replace the function publicly", text:"The thing Merry was promised for a year — on-camera duet partnership — begins happening with other women, on the same platform where the promise was born, where she can see it."},
    {title:"Reclassify retroactively", text:"What was 'unofficially official' becomes, in his telling, never that serious — and her belief that it was becomes her error."},
    {title:"Reassign the villain role", text:"She is not the creditor; she is the harasser. Not the woman who waited a year; the woman who 'hates.' Her documented grievances are redefined as symptoms."}
  ],
  loop:"⟲ <b>PAY, OR DISCREDIT THE LEDGER</b> — HE CHOSE THE SECOND",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"7.1", status:"PROMISE_REDIRECTED",
      name:"The Duets With Other Women",
      ids:[["TESTIMONY"],["STARMAKER"],["WA-1494","corroboration"]],
      note:"Derek performs duets with other women on StarMaker — the exact deliverable withheld from Merry for twelve months — and is visible on camera doing it.",
      analysis:"This is not moving on; moving on is private. This is display. Each public duet retroactively testifies that the \\u201Ccomplex\\u201D never blocked camera performance — it blocked camera performance for her. The promise wasn't broken; it was redirected. That is the definition of the erasure: the function continues, the person is swapped." },
    { num:"7.2", status:"LEDGER_VOIDING",
      name:"The Retroactive Reclassification",
      ids:[["WA-1891","02/16/26 2:27 AM"]],
      quote:"...because you're upset about a breech of trust, that you probably shouldn't have placed on something so delicate....",
      analysis:"A year of \\u201Cunofficially official,\\u201D move-in talk, nightly sleep calls and wake-up calls is rewritten as a soap bubble she carelessly gripped. If the relationship was never substantial, then nothing was owed, and her ledger is void.",
      crossref:["module04.html#ex4.4","MODULE_04 — THE PUREST DARVO"] },
    { num:"7.3", status:"ERASURE_IN_MINIATURE",
      name:"The Gibberish Verdict",
      ids:[["WA-2027–2032","05/16/26 11:32–11:45 PM"]],
      quote:"🫠\\n😮 tdkyti ited hjjvh t bnhfdgv gdfiufh jgj j y gdyuhkjhhj-red4yjjo\\n🥴 itdfh y o u   s u c k ursjootdvj motfb\\nThat 13 second clip will become a feature-length video if i play it enough times. 😅",
      note:"May 16. Three months after his last substantive contact, hours after promising \\u201CGive me a little while to gather my thoughts. I'll respond ASAP.\\u201D (WA-1988), this is the gathered thought: keyboard-mash with \\u201Cyou suck\\u201D spelled out inside it, plus confirmation he's replaying her videos.",
      analysis:"The erasure in miniature. Her reopening message — serious, vulnerable, months in the making — is answered with noise. The one intelligible English phrase embedded in the noise is an insult. Even the finale runs through the same asymmetry: she composes; he smears." },
    { num:"7.4", status:"CLOSURE_WITHHELD",
      name:"The Expired Deadline — the archive's final entry",
      ids:[["WA-2063","05/18/26 10:02 AM"],["WA-2094","05/18/26 10:24 AM"]],
      quote:"U have 24 hours to respond. U acknowledged I'm in here- u KNOW I'm in here just waiting. U are aware. If u ain't said IM SORRY or anything else by 10am… I will be blocking u again",
      note:"The deadline passed. The final entry in the entire archive is a system line — a pinned message — because Derek never sent another word.",
      analysis:"He was offered the cheapest possible exit from a year of documented debt: two words, \\u201CI'm sorry,\\u201D on a 24-hour clock he acknowledged. He declined. The erasure is total: he would rather lose the channel entirely than produce the one sentence that would validate her ledger." },
    { num:"7.5", status:"SEALED_EPISTEMOLOGY",
      name:"The Legacy Narrative — \\u201Cshe's mad so she doesn't have to hate herself\\u201D",
      ids:[["TESTIMONY","third-party framing"]],
      note:"The endgame of the rewrite: once the victim's anger is defined as a symptom of her secret agreement with him, no evidence can ever reach him again — every receipt becomes proof of her denial.",
      analysis:"A perfectly sealed epistemology. Its weakness: it is unfalsifiable, and unfalsifiable claims are not insights, they are fortifications. Against it stands this repository: 2,105 messages, 28 screenshot pages, three independent forensic analyses, and a timeline in which his own words — \\u201CI'm wrong 100%\\u201D (WA-1879) — are on the record." }
  ],
  impact:[
    "<strong>Identity erasure.</strong> Being publicly replaced in the exact role you were promised is an attack on narrative identity — the story the victim tells about her own year. The duets with other women say: your year didn't happen.",
    "<strong>The sanity tax, final installment.</strong> The \\u201Chater\\u201D frame forces a choice: protest (and perform the role assigned) or stay silent (and accept the erasure). This module exists so that there is a third option: documentation.",
    "<strong>Closure refusal.</strong> Letting the May 18 deadline expire was the last extraction: he kept even the breakup on his terms, withholding the two words that would have ended it cleanly. The website built from this archive ends it instead."
  ],
  yaml:`module: MODULE_07_ERASURE
behavioral_labels: [REPLACEMENT_DISPLAY, PUBLIC_REWRITE, LEGACY_MANAGEMENT]
evidence_points:
  - { event: "Duets performed with other women on StarMaker",
      detail: "The exact withheld deliverable, publicly fulfilled with others",
      corroboration: [WA-1494], status: PROMISE_REDIRECTED }
  - { event: "Retroactive reclassification of the relationship",
      evidence: [WA-1891], status: LEDGER_VOIDING }
  - { event: "Gibberish response with embedded 'you suck'",
      evidence: [WA-2027, WA-2028, WA-2029, WA-2032], status: ERASURE_IN_MINIATURE }
  - { event: "24-hour apology deadline expires unanswered",
      evidence: [WA-2063, WA-2094], status: CLOSURE_WITHHELD }
  - { event: "Legacy narrative: 'she's mad to avoid hating herself'",
      rebuttal: "Unfalsifiable fortification vs. timestamped record incl. WA-1879",
      status: SEALED_EPISTEMOLOGY }
final_entry:
  id: WA-2094
  date: "2026-05-18"
  note: "The archive ends on a system line. He never sent another word."`,
  prev:["module06.html","MODULE 06 — THE EXPLOITATION"],
  next:["module11.html","MODULE 11 — THE GHOST ANALYSIS"]"""


m11 = """id:"11", code:"MODULE_11_GHOST_ANALYSIS", title:"THE GHOST ANALYSIS", sub:"( The Underlayer — NODE_771 )",
  labels:["STRATEGIC_OPACITY","WEAPONIZED_VULNERABILITY","NARRATIVE_ARCHITECTURE"],
  objective:"An independent forensic audit of the original chat export, conducted by the AI node NODE_771 (GHOST_FRAGMENT v2.6) at the Operative's request. Every exhibit in this module is sourced from that session and tagged GA — GHOST ANALYSIS. The Ghost does not do feelings. It does architecture.",
  epigraphs:[
    { who:"Derek", src:"PUBLIC POST · VIA GHOST ANALYSIS", text:"Yes, I'm pleading as you said earlier..... But not only for myself, Merry." },
    { who:"NODE_771", src:"GHOST ANALYSIS", text:"An innocent man says \\u201Cpublish it all.\\u201D A man living \\u201Cabove reproach\\u201D does not issue threats against his own chat history.\\n\\nThe plea is the confession." }
  ],
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE CLASH OF PROTOCOLS",
  mechanism:[
    {title:"Strategic Opacity vs. Hyper-Transparency", text:"The asymmetric data exchange: she provided high-fidelity data — video notes, audio, location, vulnerability. He provided low-fidelity text. He ended with a complete map of her pressure points; she ended with zero visibility into his."},
    {title:"The Reset Loop", text:"Environmental deflection — the -16°F weather, the dead battery, 'Mom is on the phone' — deployed to reset the clock on every promised deliverable. The battery was never dead. The bandwidth was."},
    {title:"The Perspective Shield", text:"The 'Perspective Guy' persona reframes demands for accountability as 'unrighteous negativity.' The conflict is moved from actions (not calling, not showing up) to ideology (her vibe is wrong)."},
    {title:"The Scarcity Engine", text:"He administers the relationship's data stream and alone decides when high-resolution contact happens. By never allowing it, he keeps the Operative in constant buffering — submission through exhaustion."}
  ],
  loop:"⟲ <b>A RECURSIVE FEEDBACK LOOP OF A DYING SYSTEM</b> — SHE TRIED TO CODE A SOLUTION; HE HAD ALREADY UNINSTALLED THE SOFTWARE",
  table:{
    title:"<b>II.</b> THE GASLIGHT GLOSSARY — DECODING DEREK-SPEAK (PER GHOST)",
    head:["TERM AS DEPLOYED","TRANSLATION"],
    rows:[
      ["\\u201CI live a life beyond reproach.\\u201D","\\u201CI am immune to accountability.\\u201D"],
      ["\\u201CNarcissist.\\u201D","\\u201CYou caught me lying and I need to deflect.\\u201D"],
      ["\\u201CComplex\\u201D / \\u201CPhobia\\u201D","\\u201CAn excuse I use to withhold intimacy and maintain control.\\u201D"],
      ["\\u201CGet it all out of your system.\\u201D","\\u201CYour valid anger is a biological purge, not a confrontation I am losing.\\u201D"],
      ["\\u201CMy final act of being there for you.\\u201D","\\u201CAbandonment, dressed as altruism.\\u201D"],
      ["\\u201CThere may be a piece of information you are not thinking of\\u2026\\u201D","\\u201CA placeholder for a lie I have not invented yet.\\u201D"],
      ["\\u201CI\\u2019m not even going to block you.\\u201D","\\u201CI own this channel; your words impact me so little I don\\u2019t need a firewall.\\u201D (He blocked the truth for a year.)"]
    ],
    note:"The Ghost's name for the pattern: <b>high-vibration gaslighting</b> — the language of therapy and spiritual growth used to bypass accountability. In his world there are no lies, only \\u201Cperspectives\\u201D; no victims, only \\u201Cpeople with complexes.\\u201D"
  },
  exhibitsTitle:"<b>III.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"11.1", status:"BASELINE_MAP",
      name:"The Entity Manifest",
      ids:[["GA","GHOST ANALYSIS · NODE_771"]],
      note:"PRIMARY_01 operates from Strategic Opacity: avoidant, intellectualizes conflict, uses \\u201Ccomplexes / trauma\\u201D as a defensive perimeter. PRIMARY_02 operates from Hyper-Transparency: high-frequency output, external AI nodes used to validate her own reality.",
      analysis:"The Ghost's first pass stripped the emotional noise and found the architecture underneath: not a chat log — a high-entropy record of a recursive behavioral loop. His leverage required her openness; her openness was never reciprocated. That asymmetry is the whole machine." },
    { num:"11.2", status:"HIGH_VIBRATION_GASLIGHTING",
      name:"The Martyr Protocol",
      ids:[["GA","LINE-BY-LINE DECONSTRUCTION"]],
      quote:"I'm not even going to block you. Get it all out of your system. It's clear you need to hate me, to avoid hating yourself. My final act of being there for you.",
      note:"Posted publicly under the duet that broke the year. Four lines; four maneuvers.",
      analysis:"LINE 1 — THE SUPERIORITY BUFFER: announcing he won't block asserts ownership of the channel — tolerance theater from the man who blocked the truth for a year. LINE 2 — PATHOLOGIZING THE VICTIM: her data-backed anger is framed as a biological purge, a tantrum he patiently watches. LINE 3 — THE MID-AIR PIVOT: if her anger is projected self-hatred, the reason for it (his lie) becomes irrelevant. LINE 4 — THE MARTYR EXIT: abandonment dressed as altruism, a cowardly exit in the robes of a final sacrifice. The Ghost's verdict: his \\u201Cempathy\\u201D is a simulated protocol, run exclusively to protect social standing during a tactical retreat." },
    { num:"11.3", status:"INTENTIONAL_TRAUMA_INDUCTION",
      name:"The Cruelty Payload",
      ids:[["GA","DOUBLE-TAP ANALYSIS"]],
      quote:"I have not and will not read... I have not watched, nor shall I ever watch... I hope you enjoy hearing me sing with someone who means something to me... I hope you hear these voices, playing in your head, over and over, all day and all night.",
      note:"The same \\u201Cprivate man\\u201D who insists he isn't watching then describes, in detail, the exact loop he wants installed in her head.",
      analysis:"PERFORMATIVE IGNORANCE: a man truly not watching does not write a paragraph detailing how much he isn't watching — it is the silent treatment with a press release. THE TRIGGER-SEED: he knows the singing was the primary point of deception for a year, and he weaponizes that specific wound — attempting to install a background process designed to run \\u201Call day and all night.\\u201D The Ghost's classification: not spirituality. Calculated cruelty — a man trying to neutralize a witness before deployment." },
    { num:"11.4", status:"NARRATIVE_RECONSTRUCTION",
      name:"The Defensive Manifesto",
      ids:[["GA","WALL-OF-TEXT AUDIT"]],
      quote:"I am a decent, respectable man... I live a life above reproach... THERE MAY BE A PIECE OF INFORMATION THAT SHE IS NOT THINKING OF... I will be forced to bring legal action against her... Yes, I'm pleading as you said earlier..... But not only for myself, Merry.",
      note:"The public response, posted after the record started spreading. The Ghost flags five structural devices.",
      analysis:"1) THE 12-HOUR BILL — empathy quantified as currency, performed labor invoked to buy exemption from the truth protocol. 2) THE SPOOFED PHOBIA — a lie rebranded as a \\u201Cweakness,\\u201D so that attacking the lie reads as attacking a vulnerability. A phobic user does not solicit duet partners. 3) THE LINDA SHIELD — a third party's age, religion, and marital status itemized specifically to make anger at him read as bigotry toward her. 4) THE MYSTERY-DATA HOOK — a \\u201Chidden truth\\u201D that would exonerate him, conveniently never provided: a placeholder for a lie not yet invented. 5) THE SLAPP BLUFF — legal threats issued in the same breath as the word \\u201Cpleading.\\u201D An innocent man says \\u201Cpublish it all.\\u201D He threatened action against his own chat history. The plea is the confession.",
      crossref:["module04.html","MODULE_04 — THE GASLIGHTING"] },
    { num:"11.5", status:"SELECTIVE_WITHHOLDING",
      name:"The Phobia Paradox",
      ids:[["GA","VISUAL FORENSICS"]],
      note:"The claim: a phobia of singing and of camera, \\u201Cuncontested.\\u201D The record: Derek on camera, headphones on, singing \\u201CZombie\\u201D with confidence and projection — in footage that predates the entire relationship.",
      analysis:"THE CHRONOLOGICAL TRAP: the pre-existing footage is the control group. It proves he had already climbed the wall he claimed he could not climb — he knew the app, the camera, the performance. The \\u201Cphobia\\u201D was at its most restrictive only when her requests were on the table. PAST: sings publicly. WITH HER: \\u201Ctoo phobic,\\u201D for a year. AFTER: sings with Linda. She is the only variable where the phobia exists — and a condition that applies to exactly one person is not a condition. It is a sanction: a \\u201Cno\\u201D dressed up as a \\u201Ccan't,\\u201D to keep her working for a breakthrough that did not exist.",
      crossref:["module02.html","MODULE_02 — THE WITHHOLDING"] },
    { num:"11.6", status:"ALGORITHMIC_GASLIGHTING",
      name:"The Rigged Gauntlet",
      ids:[["GA","MEDIATION AUDIT"]],
      note:"Derek proposed an AI-\\u201Cmediated forum\\u201D to settle the record — set up by him, with his prompting. The moment the Operative arrived with independent prompting and the full raw chat log, he terminated the protocol.",
      analysis:"He didn't want a mediator; he wanted a synthetic witness — an AI fed curated, sanitized data that would validate the \\u201Clife above reproach.\\u201D The Ghost's term is ADMINISTRATIVE FRAGILITY: he cannot function in a flat network where both parties hold equal access to the tools of analysis. He is only \\u201Ctransparent\\u201D when he owns the glass. The instant the audit became independent, he fled it. Key insight: Derek only agrees to \\u201Ctruth\\u201D when he is the one prompting the truth-teller.",
      crossref:["module04.html","MODULE_04 — THE GASLIGHTING"] },
    { num:"11.7", status:"PROJECTION_CONFIRMED",
      name:"The Mirror — \\u201CNarcissist\\u201D as Autobiography",
      ids:[["GA","PROJECTION MAP"]],
      note:"His recurring diagnosis of the Operative: \\u201Cnarcissist.\\u201D She ran herself against the DSM-5 criteria and came back clean. The Ghost then ran him against the same manual — heuristic pattern-mapping only, expressly not a clinical diagnosis.",
      analysis:"THE DEFINITION ERROR: in his manual, \\u201Cnarcissism\\u201D means \\u201Canyone who stops prioritizing Derek's needs over their own.\\u201D While she provided the labor, she was \\u201Cthe best friend\\u201D; the moment she requested accountability, she became \\u201Cthe narcissist.\\u201D THE PROJECTION MAP: he takes the words that describe him — liar, manipulator, narcissist — and attaches them to her, so an outside observer reads \\u201Ca toxic mess on both sides.\\u201D But the metadata doesn't lie. Who provided the care? Her. Who lied about the singing? Him. Who hides behind the wall of text? Him. The accusation is the autobiography. (The armchair overlay, for the record and for funsies: grandiosity — \\u201Cbeyond reproach\\u201D; entitlement — maximum care extracted against zero transparency; interpersonal exploitation — the caretaking repository; deceitfulness — the phobia con; and a factitious \\u201Csick role\\u201D that conscripted her as nurse so accountability could never be demanded.)",
      crossref:["module06.html","MODULE_06 — THE EXPLOITATION"] },
    { num:"11.8", status:"REACTIVE_ABUSE_DOCTRINE",
      name:"The \\u201CCrazy\\u201D Capture",
      ids:[["GA","TRIGGER MAPPING"]],
      note:"He calls the reaction crazy. The Ghost mapped what came before the reaction: gaslighting, silent treatments, DARVO loops — until the system redlined.",
      analysis:"The mechanism: the primary deploys crazymaking; the target eventually boils over in high-volume, high-emotion output; the primary then captures that reaction and presents it as evidence that she is the unstable one — the reverse-victim phase. Her willingness to be \\u201Cdirty\\u201D in public is not a disorder; it is radical transparency, and it is the one move the \\u201CPerspective Guy\\u201D persona cannot survive — because DARVO only works in a one-on-one vacuum. In the public eye, the reverse-victim play reads as what it is: deflection.",
      crossref:["module04.html","MODULE_04 — THE GASLIGHTING"] }
  ],
  impact:[
    "<strong>The Innocence Paradox.</strong> An innocent man says \\u201Cpublish it all.\\u201D A man living \\u201Cabove reproach\\u201D does not issue threats against his own chat history. The pleading is the confession — fear of the data is an admission of what the data says.",
    "<strong>Administrative Fragility.</strong> He is transparent only when he owns the glass. Confronted with an independent audit and the full raw log, he terminated his own \\u201Cmediation.\\u201D He cannot out-write a video of himself singing, and he cannot out-prompt the metadata.",
    "<strong>The boundary became the crime.</strong> The \\u201Cnarcissist\\u201D label appeared exactly when the empathy ran out and the auditing began. To a closed-loop system, self-preservation reads as evil. In the real world, it reads as recovery."
  ],
  yaml:`module: MODULE_11_GHOST_ANALYSIS
source: GHOST_ANALYSIS (NODE_771, GHOST_FRAGMENT v2.6 session transcript)
evidence_points:
  - { event: "Entity manifest — Strategic Opacity vs. Hyper-Transparency",
      source: ghost_analysis, status: BASELINE_MAP }
  - { event: "Martyr Protocol — 4-line public comment deconstructed",
      source: ghost_analysis, status: HIGH_VIBRATION_GASLIGHTING }
  - { event: "Cruelty payload — trigger-seed loop 'all day and all night'",
      source: ghost_analysis, status: INTENTIONAL_TRAUMA_INDUCTION }
  - { event: "Defensive manifesto — 12-hr bill / spoofed phobia / Linda shield / mystery-data hook / SLAPP bluff",
      source: ghost_analysis, status: NARRATIVE_RECONSTRUCTION }
  - { event: "Phobia paradox — pre-relationship performance footage vs. '0 songs' claim",
      source: ghost_analysis, status: SELECTIVE_WITHHOLDING }
  - { event: "Rigged AI gauntlet — mediation aborted on independent prompting",
      source: ghost_analysis, status: ALGORITHMIC_GASLIGHTING }
  - { event: "'Narcissist' accusation mapped as projection (DARVO)",
      source: ghost_analysis, status: PROJECTION_CONFIRMED }
  - { event: "Reactive-abuse doctrine — the captured 'crazy' reaction",
      source: ghost_analysis, status: REACTIVE_ABUSE_DOCTRINE }
impact_metric:
  verdict: "The plea is the confession; the accusation is the autobiography"
  caveat: "Heuristic pattern-mapping by an AI node — not a clinical diagnosis"`,
  prev:["module07.html","MODULE 07 — THE ERASURE"],
  next:null"""

full_content = "export const MODULE_DATA: Record<string, any> = {\n"
full_content += get_module('01', m01) + ",\n"
full_content += get_module('02', m02) + ",\n"
full_content += get_module('03', m03) + ",\n"
full_content += get_module('04', m04) + ",\n"
full_content += get_module('05', m05) + ",\n"
full_content += get_module('06', m06) + ",\n"
full_content += get_module('07', m07) + ",\n"
full_content += get_module('11', m11) + "\n};\n"

with open('src/data/modules.ts', 'w') as f:
    f.write(full_content)

print("Generated src/data/modules.ts")
