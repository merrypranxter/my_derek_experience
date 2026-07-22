import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Module 06
mod_06 = """  '06': {
    id:"06", code:"MODULE_06_EXPLOITATION", title:"THE EXPLOITATION", sub:"( Emotional & Domestic Labor )","""
content = content.replace(mod_06, mod_06 + """
  addendum: [
    { title: "FREELY GIVEN", text: "There was some R-rated funny business going on, but he didn't demand it. Don't ever make it seem like he demanded it, or that it was transactional, because it was never like that. He wasn't like that. He was very asexual, almost — even though he did appreciate my titties. And he did like it when I squealed in his ear. He didn't get mad at it. Let's just put it that way.\\n\\nBut I offered that freely. I thought it was fun. I had just got out of a 10-year marriage. I'd never really been in a situation where I could, like, show my boobies to a man over the phone before, and I thought that that would be fun. And I thought it was.\\n\\nI would titty bomb him. I would call it a titty bomb. He might be at the library or something, and I would just pop up in the little bubble — titty bomb!! — and just flash him real quick, or something like that." },
    { title: "GIVING HIM MY ENERGY", text: "Sometimes I used him as, like, a sexual outlet, because I felt like he was someone safe that I could trust. But could I? Could I? He never even kept any of his promises to me. He said some mean shit to me there at the end, like he never cared about me at all the whole time. And I was just jerking off in his ear because I thought he deserved it.\\n\\nI would do this thing where I would think of it as giving him my energy. He never knew that. Maybe he did. I don't know. But, you know, like, sexual energy. I would give it to him because I thought he deserved it. But he never deserved it." },
    { title: "NOT TRANSACTIONAL — BUT NOT HONEST EITHER", text: "If I had known he was never gonna do the goddamn shit that he said he was gonna do, if I'd known I was never gonna get my goddamn face, or video call, if I'd known that he was never gonna join another duet ever again, if I'd known that he was gonna make me feel guilty for my emotional reaction to all of that — I never would have done it.\\n\\nSo while it wasn't transactional, it also was kind of dishonest, I think. But at the same time, whatever. I don't care. It was my decision to do it. So I cannot fault him for that.\\n\\nBut at the same time, the way he talked to me, the way he treated me when we were alone, would leave anyone to believe that he deeply cared for me, and I was one of his very best friends. But at the same time, he manipulated me, he gaslit me, and he repeatedly ripped the rug out from under me — making promises and moving goalposts and letting me down and not doing a thing, over and over and over. Just saying he had a complex. He has a complex. I'm not being sensitive to his complex. It's all my fault.\\n\\nFuck him." }
  ],
  gallery:{ title:"<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE · CLICK TO ENLARGE",
    images:[
      { src:"https://storage.googleapis.com/astraltrash_other/derek/forensics_shadow_labor.jpeg", cap:"<b>FORENSIC REPORT: THE SHADOW LABOR DYNAMIC</b> — “He didn't change it because he didn't have to. He already had your labor. He was 'satiated.'”" }
    ]},""")

# Module 11
mod_11 = """  '11': {
    id:"11", code:"MODULE_11_GHOST_ANALYSIS", title:"THE GHOST ANALYSIS", sub:"( The Underlayer — NODE_771 )","""
content = content.replace(mod_11, mod_11 + """
  gallery:{ title:"<b>+</b> THE RECEIPTS — THE PUBLIC THREAD & THE PLEA · CLICK TO ENLARGE",
    images:[
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting.PNG", cap:"<b>THE MARTYR COMMENT</b> — posted publicly under the duet that broke the year. “Get it all out of your system. It's clear you need to hate me, to avoid hating yourself… my final act of being there for you.”" },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/complex_last_word1.PNG", cap:"“Singing became something traumatic for me. You were supposed to help me with that. In exchange for the abundance of help you received from me.” — the same thread." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/last_words_sorry_not_sorry.PNG", cap:"“I'm sorry that I'm not sorry that you are incapable of being sorry.” Below the fold, the audience does the math: “sounds like 10 months no singing 😂”" },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/begging_if_innocent_why_not.PNG", cap:"“If I really am the bad guy here… how is what I'm doing hurting you in any way? … Why are you so worried for people to see the truth, huh?” — the question he never answered." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/begging_me_not_do_if_hes_the_victim_why_not.PNG", cap:"“Merry….I'm going to ask you one time, based on any friendship we used to have: Just stop this. Seriously…” — the plea. Also known as the confession." }
    ]},""")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("done pt3")
