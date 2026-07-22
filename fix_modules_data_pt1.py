import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Add gallery and addendum to 01
mod_01 = """  '01': {
    id:"01", code:"MODULE_01_PROMISES", title:"THE PROMISES", sub:"( The Hook & The Bait )","""
content = content.replace(mod_01, mod_01 + """
  addendum: [
    { title: "THE SPOT ON HIS PROFILE", text: "And it wasn't just about the duet or seeing his face. There was the whole thing about getting to be in the little spot on his StarMaker profile. The one where Jay was all the time, in the couple spot. I did not want to replace Jay. I didn't want to be there all the time. I just wanted a little representation on his profile here and there, seeing as he was plastered all over mine, and I had joined like a billion of his duets, and he hadn't joined any of mine. I just wanted something when people clicked on the little face next to mine on my StarMaker profile, and it sent me to his profile, just there to be something there. Something of me there. Anything of me there.\\n\\nAnd I only wanted five days on his little spot as his best friend. I didn't want the couple spot. I didn't want to replace Jay. She was fine. I just wanted him to like, let me up on his profile thingy for like five days here and there, or a day here and there. Fuck, I never got anything. And in the beginning, he promised me. He promised me. And every time I brought it up, it was pushed back farther and farther and farther. If I had to bring it up, that meant the goalpost got moved. Because I got punished, because he saw me as some stupid little grasshopper to his Mr. Miyagi. And that pissed me the fuck off, because it wasn't like that. But he seemed to think it was. So there was that. I never got to be in that spot.\\n\\nThe whole thing about just put some of my artwork, put a picture of me in your little photo gallery thing back there. Anything, anything. He finally made a collage of art that I'd made with our names together. No pictures or anything. I got a picture up there sometimes. But like it was always replaced very quickly by some picture Jay added that wasn't even nearly as good or creative as the one that I made that she bitched at him and demanded he put in place because she didn't like the fact that mine was there. That's how it was. Jay got catered to. When Jay threw a fit, it got catered to. When I threw a fit, I was the problem. And I needed to correct my attitude, is how that worked. Okay, well we'll go into Jay in another module." },
    { title: "THE PRECIPICE", text: "Let me think if there were any other promises. Just, I always felt like I was on the edge of a precipice. Like a thing, a good, exciting thing was about to happen, but it never did. And then I would like get excited about it. As ChatGPT put it, I inhabited these futures in my brain, and they never came true. They just never happened." },
    { title: "NICE FIRST", text: "And like at first I would try to talk him into it. I tried to be nice. I tried, I tried everything nicely I could, and it didn't work. And it's like he doesn't remember that. All he remembers is me being a bitch. I didn't resort to being a bitch till after being nice didn't work a million times. I just couldn't make him keep his promises. It's like he didn't want to. It felt like he didn't want to. It felt like I had to earn everything, but it was impossible to earn.\\n\\nAnd then when I had my inevitable emotional reaction slash autistic meltdown slash traumatic fucking response to the rug pull, to the yoink of it all, I was blamed for it all. It was my fault it wasn't happening because of my response to the fact that it didn't happen, which doesn't really seem to make sense, but somehow he made it make sense at the time. And for a while there, I went along with it, and I thought he was right. But now I realize he was fucking wrong the whole time, and *he can kiss my ass*." }
  ],
  gallery: { title:"<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE · CLICK TO ENLARGE",
    images:[
      { src:"https://storage.googleapis.com/astraltrash_other/derek/DUET_PARTNER_ORIGINAL.PNG", cap:"<b>THE ORIGINAL ASK</b> — “Will you be my officially unofficial video duet partner? 💍” — 5:01 AM. She answered inside a minute: uh FUCK YEAH." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/forensics_derek_integrity.jpeg", cap:"<b>FORENSIC AUDIT</b> — Subject B: The Selective Integritist. Promised: the duet partnership, a Thanksgiving video call, late-night video calls. Delivered: none. “Integrity status: Bankrupt/Deficient.”" },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/forensics_old_page_3.jpeg", cap:"<b>FORENSIC AUDIT</b> — “The Carrot on the Silver Platter (The Duet Partner Bait).” The audit named the same platter she did." }
    ]},""")

# Module 02 gallery
mod_02 = """  '02': {
    id:"02", code:"MODULE_02_WITHHOLDING", title:"THE WITHHOLDING", sub:"( The Control Mechanism )","""
content = content.replace(mod_02, mod_02 + """
  gallery: { title:"<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE · CLICK TO ENLARGE",
    images:[
      { src:"https://storage.googleapis.com/astraltrash_other/derek/face_promise111.PNG", cap:"<b>CHAT SEARCH: “your face”</b> — “And now you're the guy that NEVER let me see his face when he promised.” “You PROMISED. YOU PROMISED.” The face never shipped." }
    ]},""")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("done pt1")
