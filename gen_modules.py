import json

data = r"""
window.MODULE = {
  id:"01", code:"MODULE_01_PROMISES", title:"THE PROMISES", sub:"( The Hook & The Bait )",
  labels:["LOVE_BOMBING","FUTURE_FAKING"],
  objective:"The establishment of an emotional contract designed to secure maximum investment from the victim while providing zero tangible commitment from the perpetrator. (Pre-log era: user testimony + StarMaker profile + third-party reports; log-era receipts cross-referenced in MODULE_03.)",
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE BLUEPRINT OF THE SCAM",
  mechanism:[
    {title:"Find the void", text:"An eight-year aspiration for a creative and emotional anchor is identified. Derek positions himself as the sole provider of its fulfillment."},
    {title:"Offer a status, not a collaboration", text:"The 'Dedicated Duet Partner' title creates an 'unofficially official' bond that feels exclusive and special — classic future-faking. Defenses drop; emotional and sexual labor rises."},
    {title:"Stack the secondary hooks", text:"Once the primary hook is set, he adds the promise of video calls (visual intimacy) and a shared living situation (physical stability)."},
    {title:"Promises become payments", text:"Each promise functions as a 'payment' for Merry's continued patience and tolerance of his increasingly erratic behavior."}
  ],
  loop:"⟲ <b>EVERY PROMISE BUYS MORE PATIENCE</b> — YOU CANNOT PULL A RUG THAT WAS NEVER LAID. HE LAID IT.",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"1.1", status:"FRAUDULENT",
      name:"The \u201CDedicated Duet Partner\u201D Contract",
      ids:[["TESTIMONY"],["STARMAKER"],["DOSSIER §1"]],
      note:"Derek asked Merry to be his dedicated duet partner, framed as a mutual commitment to sing together and build a friendship. He performed exactly one (1) duet — \u201CThe Bedrock Anthem\u201D — then ceased all collaborative effort for an entire year.",
      analysis:"By granting one single \u201Cwin\u201D early on, he proved the promise was possible, making a year of silence read as a \u201Ctemporary hurdle.\u201D This manufactured the Sunk Cost Fallacy: she stayed because she had already invested so much in the idea of the partnership." },
    { num:"1.2", status:"MANIPULATED",
      name:"The \u201CTwo-Week\u201D Video Call Timeline",
      ids:[["TESTIMONY"],["WA-0560"],["WA-0605"]],
      note:"Derek explicitly stated that within \u201Ca couple of weeks\u201D they would have a face-to-face video call. The couple of weeks became months, then became a \u201Crule\u201D where the date was pushed back indefinitely — corroborated in-log by WA-0560 and WA-0605.",
      analysis:"The carrot on a stick. A specific but fake timeline keeps the victim in anticipatory anxiety. The promise was never intended to be kept; it was intended to be negotiated. This is the origin of the goalpost system.",
      crossref:["module03.html","MODULE_03 — THE RUG-PULLS"] },
    { num:"1.3", status:"FANTASY_CONTROL",
      name:"The \u201CMove-In\u201D Fantasy",
      ids:[["TESTIMONY"]],
      note:"Discussions occurred regarding Merry moving to Atlantic City to live with Derek. No concrete plans were ever finalized, and Derek remained unhoused and unstable throughout.",
      analysis:"High-stakes future-faking. Suggesting a shared household escalated the perceived seriousness of the relationship, ensuring she felt a level of commitment that justified providing extreme emotional support and sexual content." }
  ],
  impact:[
    "<strong>The Dopamine Loop.</strong> Every mention of the \u201Cfuture\u201D (the duet, the call, the move) triggered a dopamine release; every withholding created withdrawal. The cycle is identical to the mechanics of gambling addiction.",
    "<strong>The Erasure of Self.</strong> Because the \u201Cpartnership\u201D was the center of the relationship, Merry began to define her value by her ability to \u201Cearn\u201D the duet or the call. She transitioned from a creator to a supplicant.",
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
  perpetrator_gain: "Maximum emotional labor / Sexual compliance"`,
  prev:null,
  next:["module02.html","MODULE 02 — THE WITHHOLDING"]
};
---
window.MODULE = {
  id:"02", code:"MODULE_02_WITHHOLDING", title:"THE WITHHOLDING", sub:"( The Control Mechanism )",
  labels:["SENSORY_DEPRIVATION","COERCIVE_CONTROL","EMOTIONAL_STARVATION"],
  objective:"To maintain a power imbalance by identifying the victim's primary communication needs and systematically denying them, thereby forcing her into a state of dependency and desperation.",
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
      note:"Merry requires visual input to overcome auditory processing issues and a thick New Jersey accent. Derek refused video calls, bubbles, or any visual accompaniment — allowing her to spend 40% of their hours-long conversations saying \u201CHuh? What? Say that again\u201D without offering the simplest solution.",
      analysis:"Cognitive sabotage. Constant low-grade confusion is a prime state for manipulation: he limited the data she could receive to make her dependent on his interpretation of it." },
    { num:"2.2", status:"FRAUDULENT_VULNERABILITY",
      name:"The \u201CComplex\u201D as a Shield",
      ids:[["TESTIMONY"],["STARMAKER"],["WA-1135","12/29/25"],["WA-1494","01/22/26"]],
      quote:"Video call, 1 hr  —  system record WA-1135\nVideo call, 55 min —  system record WA-1494",
      note:"He claimed a \u201Ccomplex\u201D made camera performance impossible. He was visible on camera in old StarMaker videos, later performed duets with other women — and held two long video calls with Merry, one just seventeen days after declaring a video call would \u201Cnever happen between us.\u201D",
      analysis:"Fraudulent vulnerability: a fake weakness used to exert real power. The \u201Ccomplex\u201D was situational — it existed only when it served as an excuse to deny her, and it made the conversation about his trauma rather than her needs.",
      crossref:["module03.html#ex3.6","MODULE_03 — THE CAPABILITY RECEIPTS"] },
    { num:"2.3", status:"BREADCRUMBING",
      name:"The \u201CRations\u201D System",
      ids:[["TESTIMONY"]],
      note:"Derek would occasionally send old photos of himself, which Merry jokingly referred to as \u201Crations.\u201D",
      analysis:"Intermittent reinforcement. Small, controlled glimpses of his face — the \u201Ccrumbs\u201D of affection — make the starvation feel like a challenge rather than abuse. It mirrors captor/addict dynamics exactly." }
  ],
  impact:[
    "<strong>Sensory Frustration & Exhaustion.</strong> Hours of decoding a muffled voice without visual cues leads to sensory overload and cognitive fatigue — leaving her too exhausted to challenge his narratives or notice red flags.",
    "<strong>The \u201CSavior\u201D Paradox.</strong> Because Derek was the only one providing the \u201Cmorning calls\u201D and \u201Cemotional support,\u201D she felt she had to accept the withholding as the price of the safety he provided.",
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
  next:["module03.html","MODULE 03 — THE RUG-PULLS"]
};
---
window.MODULE = {
  id:"03", code:"MODULE_03_RUG_PULLS", title:"THE RUG-PULLS", sub:"( The Neurological Trigger )",
  labels:["GOALPOST_MOVING","INTERMITTENT_REINFORCEMENT","PUNITIVE_RESET"],
  objective:"To convert every concrete promise into a moving target, so that fulfillment is always one apology, one behavior-fix, one \u201Cright feeling\u201D away — and to weaponize the resulting destabilization (especially against a neurodivergent need for predictability) as proof that the victim is \u201Ctoo much.\u201D",
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
      analysis:"This is the goalpost literally dissolving. There is no date to miss when the date is \u201Cwhen I feel like it.\u201D She circled this exchange in the screenshot dossier because it is the whole system in one line." },
    { num:"3.3", status:"PROMISE_LAUNDERING",
      name:"The \u201CConsideration\u201D Speech — the promise becomes a wage (and then a confession)",
      ids:[["WA-0605","12/12/25 9:23 AM"]],
      quote:"When you can make, / or even just display, / one single consideration / in an outward direction / then I will continue to make sure someone is placing considerations into this pre-existing complex [...] I will PROMISE just as readily, that a video call will never happen between us, to protect my progress from you.",
      note:"Fourteen minutes after WA-0560, Derek formalizes the contingency into a contract of emotional labor: display consideration → earn a promise. But the full sentence is worse than a wage. Buried mid-clause he states the actual endgame — her need is, in his own words, the thing his \u201Cprogress\u201D must be protected from.",
      analysis:"Promise-laundering with a confession inside. The original debt is written off and replaced with a new currency in which she must now earn his willingness to re-promise — while the sentence itself quietly converts \u201Cnot yet\u201D into \u201Cnever.\u201D The arrears vanish; the ledger resets with her in the red; and the goalpost was never on the field at all." },
    { num:"3.4", status:"TRIANGULATION_THREAT",
      name:"The Replacement Threat",
      ids:[["WA-0654","12/12/25 9:36 AM"]],
      quote:"I'll tell you what.....I'll find a FRIEND who will help me work on my complexes, not make them worse. Then once I'm comfortable on camera, I'll come back & chat & sing & be well-adjusted & happy",
      analysis:"The rug-pull now has teeth. Not only is the promise withdrawn — it will be fulfilled with someone else first, and she will watch. (He follows through on exactly this: see MODULE_07, the duets with other women.) The threat converts her protest into a competition she can lose.",
      crossref:["module07.html","MODULE_07 — THE ERASURE"] },
    { num:"3.5", status:"PUNITIVE_RESET",
      name:"The Punitive Freeze — 8 days of silence after the confrontation",
      ids:[["WA-0958","emoji wall"],["WA-0995–0996","double missed calls"],["WA-1018","12/24"]],
      note:"After the Dec 12 confrontation, Derek goes silent for 8 days, then resurfaces Dec 20–23 with emoji walls and double missed calls — no acknowledgment of the confrontation, the promise, or the freeze. On Dec 24: \u201COr a dropped call...\u201D",
      analysis:"The punitive reset executed in calendar form. The confrontation cost her 8 days; its resolution cost him nothing — he re-enters as if continuity were never broken. The emoji wall is a presence-token: minimum viable contact, maximum plausible deniability." },
    { num:"3.6", status:"CAPABILITY_RECEIPT",
      name:"The Capability Receipts — TWO video calls after a year of \u201Cthe complex\u201D",
      ids:[["WA-1135","12/29/25 9:53 PM"],["WA-1494","01/22/26 1:17 AM"],["WA-1496","voice, 7 min"],["WA-1499","voice, 39 min"]],
      quote:"Video call, 1 hr  —  system record WA-1135\nVideo call, 55 min —  system record WA-1494",
      note:"After a full year in which a video call was structurally impossible due to \u201Cthe complex\u201D — and just 17 days after the Dec 12 speeches in which the call would only happen \u201Cwhen it doesn't feel like this\u201D (WA-0560) and would in fact \u201Cnever happen between us\u201D (WA-0605) — Derek gets on a one-hour video call. Then, mid-January-thaw, a second one at 1 AM.",
      analysis:"The single most corrosive fact for the \u201Ccomplex\u201D narrative — twice over. The barrier was never capability; it was leverage. The calls happened when they cost him nothing and bought maximum goodwill — and could be withheld again the moment each thaw ended. Which they were." },
    { num:"3.7", status:"GOALPOST_REMOVED_FROM_FIELD",
      name:"The Final Dissolution — withdrawal as \u201Cdelivering my conquered complex\u201D",
      ids:[["WA-1906","02/16/26 2:31 AM"]],
      quote:"So I end up choosing to withdraw / In other to — / 1.) Not be a facilitator, enabler, conduit of unrighteous unnecessary negativity / 2.) To have a better chance at repairing the breech of trust, by delivering to you, my conquered complex.",
      analysis:"The end-state of the system: disappearance rebranded as progress on the promise itself. He is not ghosting her — he is \u201Cworking on the complex,\u201D offstage, indefinitely, and any objection is \u201Cunrighteous unnecessary negativity.\u201D The goalpost has left the field entirely." }
  ],
  impact:[
    "<strong>Manufactured instability.</strong> Each cycle (offer → condition → reset → reframe) teaches the nervous system that stated plans are fiction. For a neurodivergent person this is not metaphorically destabilizing — it is a direct attack on the mechanism used to regulate.",
    "<strong>The meltdown as product.</strong> The Dec 12 logs (SC-01–28) show the output: hours of escalating distress from Merry, met with calm, formatted, sermon-like paragraphs from Derek. The asymmetry is then harvested — her volume becomes his evidence.",
    "<strong>The debt that can never be called in.</strong> By Feb 2026 the promise has been so thoroughly laundered (offer → condition → wage → threat → freeze → offstage \u201Cconquering\u201D) that any demand for fulfillment sounds, in his framing, like cruelty toward a man \u201Cworking on himself.\u201D"
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
  next:["module04.html","MODULE 04 — THE GASLIGHTING"]
};
---
window.MODULE = {
  id:"04", code:"MODULE_04_GASLIGHTING_DARVO", title:"THE GASLIGHTING", sub:"( The Reality Rewrite — DARVO: Deny, Attack, Reverse Victim & Offender )",
  labels:["GASLIGHTING","DARVO","TONE_POLICING","REALITY_REWRITE"],
  objective:"To make the victim's perception the problem. Every injury she names is converted into evidence of her defect — her tone, her \u201Cperspective,\u201D her cruelty, her instability — until she is defending her sanity instead of his record. The Feb 16, 2026 session (2:17–3:52 AM) is the machine running at full power.",
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE REWRITE MACHINE",
  mechanism:[
    {title:"Bait the reaction", text:"Withhold, disappear, move the goalpost (Modules 2–3) until the victim — autistic, sleep-deprived from phone labor, a year into broken promises — reacts with volume."},
    {title:"Discard the substance, indict the style", text:"Her content (\u201Cyou broke a year of promises\u201D) is never answered. Her delivery (\u201Cyou said fuck you\u201D) becomes the entire trial."},
    {title:"Crown himself the injured party", text:"He is the one with complexes, traumas, overwhelm; she is the \u201Cfacilitator of unrighteous negativity.\u201D Offender and victim swap seats — in writing, calmly, with bullet points."}
  ],
  loop:"⟲ <b>DENY · ATTACK · REVERSE</b> — THE MACHINE RUNS ON HER DISTRESS",
  exhibitsTitle:"<b>II.</b> THE EXHIBITS — EVERY STAGE, QUOTED VERBATIM",
  exhibits:[
    { num:"4.1", status:"DENY",
      name:"The disappearance was her accommodation failure",
      ids:[["WA-1688","02/15/26 4:08 PM"],["WA-1684","11 days silent"],["WA-1663–1671","proof-of-life calls"]],
      quote:"The Whatsapp thing is just too much when I'm overwhelmed..... and the video message thing is just 🙈🔫 / We all have our complexes, Merry / Ours just happen to clash sometimes / But I wouldn't even think the words 'fuck you' when they do / Because they are clashing / Not us",
      note:"He has just returned from 11 days of total silence, during which she sent audio messages into the void and made 4-second \u201Cproof of life\u201D calls because she was worried he was dead.",
      analysis:"The event under review is an 11-day disappearance. His opening move erases it: the real subject is her \u201Cfuck you.\u201D The disappearance becomes weather (\u201Ccomplexes clashing\u201D); her fear-response becomes the crime." },
    { num:"4.2", status:"PSEUDO_ACCOUNTABILITY",
      name:"The Past-Tense Confession — \u201CI'm wrong 100%\u201D (terms & conditions apply)",
      ids:[["WA-1879","02/16/26 2:17 AM"]],
      quote:"'was' & 'wasn't' ← Those I'm taking full responsibility for. And I would like to remedy those shortcomings (despite the fact that they're directly linked to traumas & complexes, which should be taken into consideration… It's on me / I'm wrong 100%",
      analysis:"It looks like the confession she begged for. Read the grammar. Responsibility is accepted only for the past tense — and immediately discounted by the parenthetical. Technically an admission; functionally a plea bargain." },
    { num:"4.3", status:"DENY",
      name:"\u201CThe guilt game\u201D — present and future declared negotiable",
      ids:[["WA-1885","02/16/26 2:24 AM"]],
      quote:"'isn't'  'is'  'will be'  'won't be' / ↑ These are up for grabs ↑ / in the guilt game / I understand what you're saying. I understand your rationality on things. But there's a major piece of the puzzle you're simply not seeing here.",
      analysis:"Seven minutes after \u201CI'm wrong 100%,\u201D he carves out everything that is, will be, and won't be — the entire living relationship — as contestable. Then the pivot: she is missing \u201Ca major piece of the puzzle.\u201D Her rationality is acknowledged and overruled in the same breath." },
    { num:"4.4", status:"REVERSE_VICTIM_OFFENDER",
      name:"Reverse — her trust was the original sin",
      ids:[["WA-1891","02/16/26 2:27 AM"]],
      quote:"If you compound someone's complex, because you're upset about a breech of trust, that you probably shouldn't have placed on something so delicate.... you end up compounding how upset you are because it's going to be more difficult to repair or reverse that breech.",
      analysis:"The purest DARVO in the archive. He broke trust. She got upset. His verdict: the upset is her fault for having placed trust \u201Con something so delicate.\u201D The offender is the man who broke the promise; the offender, in his telling, is the woman who believed it.",
      crossref:["module07.html#ex7.2","MODULE_07 — THE RETROACTIVE RECLASSIFICATION"] },
    { num:"4.5", status:"ATTACK",
      name:"\u201CThe perspective guy\u201D — self-appointed editor of her reality",
      ids:[["WA-1903","02/16/26 2:29 AM"],["WA-0366","12/09/25"]],
      quote:"You just lack some perspective on things / I know it sucks, but I HAVE to be the perspective guy. / And I can't allow you to say things that you shouldn't hear yourself saying out loud!",
      analysis:"Three moves in three lines: her perception is deficient; he is the corrective authority; censorship is framed as protection. He is not arguing her facts are wrong — he is asserting jurisdiction over what she may think and say. The perspective defense is a fixed habit, not a one-off." },
    { num:"4.6", status:"REVERSE_VICTIM_OFFENDER",
      name:"The Moral Exit — withdrawal as hygiene",
      ids:[["WA-1906","02/16/26 2:31 AM"]],
      quote:"So I end up choosing to withdraw / In other to — / 1.) Not be a facilitator, enabler, conduit of unrighteous unnecessary negativity / 2.) To have a better chance at repairing the breech of trust, by delivering to you, my conquered complex.",
      analysis:"Having denied, attacked, and reversed, he exits as the virtuous party. Her pain is \u201Cunrighteous unnecessary negativity\u201D; his silence is a gift in progress. This is the same withdrawal that lasted until May." },
    { num:"4.7", status:"GASLIGHT_FRAME",
      name:"\u201CI only set the stage\u201D — the gaslighter's stage direction",
      ids:[["WA-1975","02/16/26 3:52 AM"]],
      quote:"I only set the stage / Now you go and add to that stage / Or make an appeal to alter what I tried to objectively set up, granted, from my perspective",
      analysis:"The closing frame: his narrative is \u201Cobjective\u201D set design; her account is an \u201Cappeal\u201D that may be filed for review. The epistemic hierarchy is total — he authors reality, she petitions it." },
    { num:"4.8", status:"LEGACY_GASLIGHT",
      name:"The Post-Log Thesis — \u201Cshe's mad so she doesn't have to hate herself\u201D",
      ids:[["TESTIMONY","third-party framing"]],
      note:"Derek's post-breakup claim: Merry's anger is self-deception — she knows he's right and performs rage to avoid self-hatred.",
      analysis:"Rage-avoidance theories are unfalsifiable — that is their function. What is falsifiable is the record: 11-day silences, a year-old promise converted to \u201Cwhen it doesn't feel like this,\u201D a confession revoked within seven minutes, and a 55-minute video call proving the impossible was always possible. Her anger has timestamps. His \u201Crightness\u201D has none." }
  ],
  impact:[
    "<strong>Reality debt.</strong> Each cycle forces the victim to choose between her memory and the relationship. Choosing the relationship means retro-editing her own perceptions — the core injury of gaslighting.",
    "<strong>The tone tax.</strong> Because only her delivery is ever tried, she must modulate the expression of legitimate grievance until it is palatable to the person who caused it — a second job, performed during injury.",
    "<strong>Confession exhaustion.</strong> \u201CHe admitted he was wrong\u201D is not exculpatory: admissions were issued in the past tense, discounted by trauma-clauses, and revoked for the present within seven minutes."
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
  next:["module05.html","MODULE 05 — THE TRIANGULATION"]
};
---
window.MODULE = {
  id:"05", code:"MODULE_05_TRIANGULATION", title:"THE TRIANGULATION", sub:"( The Jay Hierarchy )",
  labels:["TRIANGULATION","HIERARCHY_GAMES","JEALOUSY_INDUCTION"],
  objective:"To keep the victim in a permanent audition for a rank she can never confirm, by maintaining a visible third party above her on the ladder. (Evidence status: primarily testimony and third-party reports — the Jay material lives mostly in the missing first-ten-months era; log receipts cited where they exist.)",
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE LADDER",
  mechanism:[
    {title:"Name the ranks", text:"\u201CThe Couple Spot\u201D on top — public, romantic, where duets and visible affection live. \u201CThe Best Friend Spot\u201D below — intimate, private, load-bearing. Merry's rank."},
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
      note:"Derek articulated a hierarchy of attachment — \u201Ccouple spot\u201D vs. \u201Cbest friend spot\u201D — and placed Merry in the lower one while extracting couple-tier labor from her (nightly calls, sexual content, future-planning; see MODULE_06).",
      analysis:"Naming the ranks is the tell. Casual favoritism happens; a titled hierarchy is a management system. It converts jealousy from an emotion into a job description — she now knows exactly which promotion she's working toward, and exactly who holds it." },
    { num:"5.2", status:"GRIEVANCE_IMMUNITY_DEVICE",
      name:"The Cancer Shield",
      ids:[["TESTIMONY"]],
      note:"Jay was described as dying of cancer — making any objection to her priority position an act of monstrous insensitivity.",
      analysis:"The shield does double duty. It excuses Derek's attention to Jay (\u201Chow could I abandon a dying woman?\u201D) and pre-convicts Merry (\u201Cyou'd begrudge a dying woman?\u201D). Any grievance about the hierarchy becomes proof of her cruelty — the same reversal machinery as MODULE_04, run through a third party." },
    { num:"5.3", status:"EXCLUSIVITY_FRAUD",
      name:"The Flirtation Contrast",
      ids:[["TESTIMONY"],["FORENSIC_PATTERN_ANALYSIS"]],
      note:"Sexual and flirtatious messages directed at Jay, contrasted against the framing that Merry's own sexual labor was special and exclusive.",
      analysis:"The exclusivity was the product being sold to Merry — the \u201Cunofficially official\u201D bond. The contrast is the invoice: the same currency was circulating elsewhere. Discovery doesn't end the arrangement; it intensifies it, because now she must compete." },
    { num:"5.4", status:"TRIANGULATION_ON_RECORD",
      name:"The Replacement Threat Made Concrete",
      ids:[["WA-0654","12/12/25 9:36 AM"]],
      quote:"I'll find a FRIEND who will help me work on my complexes, not make them worse. Then once I'm comfortable on camera, I'll come back & chat & sing & be well-adjusted & happy",
      analysis:"In the middle of the Dec 12 confrontation, Derek reaches directly for the triangulation lever: your slot is fillable, and the next occupant will get the camera time you bled for. It is the Jay hierarchy re-declared on the record — the promise that replacement is always one \u201Cfriend\u201D away. He later fulfills it visibly.",
      crossref:["module07.html","MODULE_07 — THE ERASURE"] }
  ],
  impact:[
    "<strong>Permanent audition.</strong> A titled rank below the top converts attachment into performance review. The victim's question shifts from \u201Cis this relationship good?\u201D to \u201Chow do I get promoted?\u201D — a question the perpetrator alone grades.",
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
      detail: "Sexual energy at Jay while exclusivity sold to Merry",
      source: user_testimony, status: EXCLUSIVITY_FRAUD }
  - { event: "Replacement threat during Dec 12 confrontation",
      evidence: [WA-0654], status: TRIANGULATION_ON_RECORD,
      cross_ref: [MODULE_03_RUG_PULLS, MODULE_07_ERASURE] }
impact_metric:
  victim_state: "Permanent audition / swallowed grievances / competitive bonding"
  perpetrator_gain: "Two-directional loyalty extraction; grievances neutralized by the shield"`,
  prev:["module04.html","MODULE 04 — THE GASLIGHTING"],
  next:["module06.html","MODULE 06 — THE EXPLOITATION"]
};
---
window.MODULE = {
  id:"06", code:"MODULE_06_EXPLOITATION", title:"THE EXPLOITATION", sub:"( Emotional & Sexual Labor )",
  labels:["LABOR_EXTRACTION","ASYMMETRIC_INVESTMENT","SERVICE_RELATIONSHIP"],
  objective:"To run the relationship as a one-way service economy: maximum emotional, domestic, and sexual output extracted from the victim; minimum — approaching zero — returned. The labor claims from the pre-log era are testimony; the log era supplies the arithmetic.",
  mechanismTitle:"<b>I.</b> THE MECHANISM — THE SERVICE ECONOMY",
  mechanism:[
    {title:"Nightly phone labor", text:"Hours on the phone every night, including sleeping on the phone — despite her stated 'caged animal' sensory aversion to telephone calls. She did it anyway. That is not a preference; that is a shift."},
    {title:"Morning wake-up calls", text:"An alarm-clock function performed daily, on his schedule."},
    {title:"Sexual labor", text:"Sexual content and flirtation provided on demand, sold as the intimacy of the 'unofficially official' bond."},
    {title:"The Alabama housing offer", text:"Actual residency offered — a roof, a state line, a life. The single largest asset class a person can put on a table."}
  ],
  loop:"⟲ RETURNED THE OTHER WAY: <b>ONE DUET, PHOTO \u201CRATIONS,\u201D A 55-MINUTE CALL, AND A 63% SILENCE RATE</b>",
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
    note:"Read the first rows again in the context of the \u201Ccomplex\u201D: the man who found WhatsApp \u201Cjust too much when I'm overwhelmed\u201D (WA-1688) was the recipient of <b>4.5×</b> more messages than he sent. The overwhelm was selective. It never once prevented him from <b>receiving</b> the labor."
  },
  exhibitsTitle:"<b>III.</b> THE EXHIBITS — DEALT ONTO THE RECORD",
  exhibits:[
    { num:"6.1", status:"ONE_WAY_ACCOMMODATION",
      name:"The Phone Labor",
      ids:[["TESTIMONY"],["WA-0212","1 hr"],["WA-1226","2 hr"],["WA-1419","4 hr"],["WA-1538","2 hr"],["WA-1494–1499","Jan 22 cluster"]],
      note:"Hours-long nightly calls, overnight sleep calls, wake-up calls — performed despite a documented sensory aversion to phone communication.",
      analysis:"The call durations alone refute the framing that contact burdened him. When the contact was audio — the format that served him and strained her — he had unlimited capacity. The burden only ever materialized around the format that served her (video)." },
    { num:"6.2", status:"EXTRACTION_AGAINST_UNDELIVERED_COLLATERAL",
      name:"The Sexual Labor & False Exclusivity",
      ids:[["TESTIMONY"]],
      note:"Sexual content and flirtation on demand, framed as the special currency of their exclusive bond.",
      analysis:"Sexual labor was the highest-interest payment in the economy — extracted against collateral (the duet, the call, the move-in) that was never delivered. In lending terms: he collected on a loan he never issued.",
      crossref:["module05.html","MODULE_05 — THE EXCLUSIVITY FRAUD"] },
    { num:"6.3", status:"RESCUE_DIRECTION_REVERSAL",
      name:"The Alabama Offer",
      ids:[["TESTIMONY"]],
      note:"Actual housing — Merry offered Derek a place to live in Alabama while he was unhoused and unstable.",
      analysis:"Note the direction of rescue. The relationship's mythology cast Derek as the provider of stability. In material reality, the only concrete housing offer ever made in this relationship ran from the victim to the perpetrator — and even that was not honored with follow-through." },
    { num:"6.4", status:"EXTRACTION_REFLEX",
      name:"The Reunion Extraction Attempt",
      ids:[["WA-1987–2032","05/16/26"],["WA-2063","24-hr deadline"],["WA-2094","expired"]],
      quote:"First of all — You look great 💯 Like.......you look really healthy.\nThat 13 second clip will become a feature-length video if i play it enough times. 😅",
      note:"After three months of silence, Merry reopens the channel. Derek's entire substantive engagement: a compliment on her body and confirmation he is replaying her video content. No acknowledgment of the rupture, no apology, no answers.",
      analysis:"The extraction reflex survives even the relationship: immediate re-consumption of her image and labor. When she issues a 24-hour deadline for an actual response (WA-2063), he lets it expire (WA-2094)." }
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
  - { event: "Sexual labor under false exclusivity", source: user_testimony,
      cross_ref: MODULE_05_TRIANGULATION, status: EXTRACTION_AGAINST_UNDELIVERED_COLLATERAL }
  - { event: "Alabama housing offer (victim → perpetrator)", source: user_testimony,
      status: RESCUE_DIRECTION_REVERSAL }
  - { event: "Reunion re-consumption without repair",
      evidence: [WA-1987, WA-2032, WA-2063, WA-2094], status: EXTRACTION_REFLEX }
impact_metric:
  victim_state: "Caregiver capture / escalating sunk cost"
  perpetrator_gain: "Full-service support at ~2% performance rate (per Forensic Audit Dossier scoreboard)"`,
  prev:["module05.html","MODULE 05 — THE TRIANGULATION"],
  next:["module07.html","MODULE 07 — THE ERASURE"]
};
---
window.MODULE = {
  id:"07", code:"MODULE_07_ERASURE", title:"THE ERASURE", sub:"( The Final Betrayal )",
  labels:["REPLACEMENT_DISPLAY","PUBLIC_REWRITE","LEGACY_MANAGEMENT"],
  objective:"To replace the victim publicly, retroactively reclassify the relationship, and install a final narrative in which the perpetrator is the wronged party and the victim is \u201Cthe hater.\u201D The perpetrator has a year of debts on the books and a witness who kept receipts. There are only two solutions — pay, or discredit the ledger.",
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
      analysis:"This is not moving on; moving on is private. This is display. Each public duet retroactively testifies that the \u201Ccomplex\u201D never blocked camera performance — it blocked camera performance for her. The promise wasn't broken; it was redirected. That is the definition of the erasure: the function continues, the person is swapped." },
    { num:"7.2", status:"LEDGER_VOIDING",
      name:"The Retroactive Reclassification",
      ids:[["WA-1891","02/16/26 2:27 AM"]],
      quote:"...because you're upset about a breech of trust, that you probably shouldn't have placed on something so delicate....",
      analysis:"A year of \u201Cunofficially official,\u201D move-in talk, nightly sleep calls and wake-up calls is rewritten as a soap bubble she carelessly gripped. If the relationship was never substantial, then nothing was owed, and her ledger is void.",
      crossref:["module04.html#ex4.4","MODULE_04 — THE PUREST DARVO"] },
    { num:"7.3", status:"ERASURE_IN_MINIATURE",
      name:"The Gibberish Verdict",
      ids:[["WA-2027–2032","05/16/26 11:32–11:45 PM"]],
      quote:"🫠\n😮 tdkyti ited hjjvh t bnhfdgv gdfiufh jgj j y gdyuhkjhhj-red4yjjo\n🥴 itdfh y o u   s u c k ursjootdvj motfb\nThat 13 second clip will become a feature-length video if i play it enough times. 😅",
      note:"May 16. Three months after his last substantive contact, hours after promising \u201CGive me a little while to gather my thoughts. I'll respond ASAP.\u201D (WA-1988), this is the gathered thought: keyboard-mash with \u201Cyou suck\u201D spelled out inside it, plus confirmation he's replaying her videos.",
      analysis:"The erasure in miniature. Her reopening message — serious, vulnerable, months in the making — is answered with noise. The one intelligible English phrase embedded in the noise is an insult. Even the finale runs through the same asymmetry: she composes; he smears." },
    { num:"7.4", status:"CLOSURE_WITHHELD",
      name:"The Expired Deadline — the archive's final entry",
      ids:[["WA-2063","05/18/26 10:02 AM"],["WA-2094","05/18/26 10:24 AM"]],
      quote:"U have 24 hours to respond. U acknowledged I'm in here- u KNOW I'm in here just waiting. U are aware. If u ain't said IM SORRY or anything else by 10am… I will be blocking u again",
      note:"The deadline passed. The final entry in the entire archive is a system line — a pinned message — because Derek never sent another word.",
      analysis:"He was offered the cheapest possible exit from a year of documented debt: two words, \u201CI'm sorry,\u201D on a 24-hour clock he acknowledged. He declined. The erasure is total: he would rather lose the channel entirely than produce the one sentence that would validate her ledger." },
    { num:"7.5", status:"SEALED_EPISTEMOLOGY",
      name:"The Legacy Narrative — \u201Cshe's mad so she doesn't have to hate herself\u201D",
      ids:[["TESTIMONY","third-party framing"]],
      note:"The endgame of the rewrite: once the victim's anger is defined as a symptom of her secret agreement with him, no evidence can ever reach him again — every receipt becomes proof of her denial.",
      analysis:"A perfectly sealed epistemology. Its weakness: it is unfalsifiable, and unfalsifiable claims are not insights, they are fortifications. Against it stands this repository: 2,105 messages, 28 screenshot pages, three independent forensic analyses, and a timeline in which his own words — \u201CI'm wrong 100%\u201D (WA-1879) — are on the record." }
  ],
  impact:[
    "<strong>Identity erasure.</strong> Being publicly replaced in the exact role you were promised is an attack on narrative identity — the story the victim tells about her own year. The duets with other women say: your year didn't happen.",
    "<strong>The sanity tax, final installment.</strong> The \u201Chater\u201D frame forces a choice: protest (and perform the role assigned) or stay silent (and accept the erasure). This module exists so that there is a third option: documentation.",
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
  next:null
};
"""

modules_js = []
for p in data.split("---"):
    p = p.strip()
    if p:
        p = p.replace("window.MODULE = ", "")
        if p.endswith(";"):
            p = p[:-1]
        modules_js.append(p)

ts_content = "export const MODULE_DATA: Record<string, any> = {\n"
for mod in modules_js:
    import re
    m = re.search(r'id:\s*"(\d+)"', mod)
    if m:
        id = m.group(1)
        ts_content += f"  '{id}': {mod},\n"
ts_content += "};\n"

with open('src/data/modules.ts', 'w') as f:
    f.write(ts_content)

