import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Module 04 gallery
mod_04 = """  '04': {
    id:"04", code:"MODULE_04_GASLIGHTING_DARVO", title:"THE GASLIGHTING", sub:"( The Reality Rewrite — DARVO: Deny, Attack, Reverse Victim & Offender )","""
content = content.replace(mod_04, mod_04 + """
  gallery:{ title:"<b>+</b> THE RECEIPTS — THE FINAL THREAD, IN HIS OWN WORDS · CLICK TO ENLARGE",
    images:[
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting222.PNG", cap:"“You're wrong, Merry. You are wrong.” — the reality verdict, delivered from the bench." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting333.PNG", cap:"“I LITERALLY spent day after day, week after week, concerned about you…” — the martyr ledger, itemized." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting444.PNG", cap:"“when we met, I was at the lowest point in my life but I still tried to be there for you” — the sympathy pivot." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting555.PNG", cap:"“everything you're upset about is internal. not a soul on the planet is going to agree with you.” — the crime scene relocated inside her skull." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting55555.PNG", cap:"“I honestly thought you would eventually come to realize that. the fact that you haven't is telling” — the disappointment frame." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/complex_gaslighting.PNG", cap:"“my life would be better if I was able to sing with you, to get over my complexes… But you didn't let me. you didn't help me.” — the debt inverted." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_complex333.PNG", cap:"“my being on video complex.” — the complex, deployed as a period at the end of the argument." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_guilt_complex.PNG", cap:"“I'm not scared, Merry. I'm hurt.” — the hurt shield, held up against the receipts." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_energyvampire.PNG", cap:"“lol what? what did I gain from manipulating you Merry ffsake, I give up” — exhaustion theater from the man with the 63% silence rate." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_fuckhim.PNG", cap:"“that's the day everything changed — when Mary had to stop being selfish.” Third person. Her name is Merry." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_narcissism.PNG", cap:"“own it.” + “I challenge you to an adult healthy well-adjusted fair debate” — the rigged gauntlet, self-described." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_pain_level15.PNG", cap:"“You are trying to hurt me at level 100. Because I couldn't avoid hurting you at level 15.” — the arithmetic of reverse victimhood." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_pain_level15_2_and_narcissism.PNG", cap:"“you still like that because you're a narcissist. 💯 I'm not trying to be mean.”" },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/gaslighting_trying_to_hurt_me.PNG", cap:"“Crazy people don't know they're crazy. And Narcs lie to themselves about being Narcs.” — the armchair, in his own hand." },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/forensics_old_honesty_derek.jpeg", cap:"<b>FORENSIC AUDIT</b> — Honesty vs. Sincerity Report: “Derek's 'honesty' is an Internalized Narrative; your 'honesty' is a Verifiable Fact.”" }
    ]},""")

# Module 05
mod_05 = """  '05': {
    id:"05", code:"MODULE_05_TRIANGULATION", title:"THE TRIANGULATION", sub:"( The Jay Hierarchy )","""
content = content.replace(mod_05, mod_05 + """
  addendum: [
    { title: "NOT THE JEALOUS TYPE", text: "I am not the jealous type. I never wanted to steal him from anyone. I never intended to be exclusive with him in any way. It was not romantic. Even though it was very flirty, and sometimes R-rated at times, it was not romantic at all. It was very much a friendship — I thought, at least.\\n\\nI never wanted to steal him from Jay. I just wanted to be his friend too. We could have all been friends. If we were on the phone and he got a call from Izzy, or a call from Jay — even though fuck that bitch — I didn't get weird about it. I didn't even feel any type of way about it. It's like, okay, bye. Talk to you later. I did not give a single fuck. I just wanted to be his friend. He could still be friends with them. I wasn't trying to steal him." },
    { title: "THE WORRY HE PERFORMED", text: "But other people acted weird about us. And he acted weird about us. He was so worried about what those girls thought. So worried. And he would always talk about how I might be in danger from some of them, LOL. He acted all worried, like one of them might come stalk me or something.\\n\\nBitch, I don't even care what they think. They can talk shit about me. They can say whatever they want. He acted like he was worried for me, but I wasn't worried. He acted like I should be worried. I just didn't know enough to be worried. I think it was mostly an act to make himself seem overly important — but I'm not sure. He does look like he does. He is a hottie. Girls do act weird like that about him." },
    { title: "IT WAS NEVER ABOUT LINDA", text: "Especially at the end — after I left, and he crawled back on that fucking app and sang with a girl that wasn't me. I'm not mad at the girl. I wouldn't have cared at all if he had just sang with me, like he promised. What I'm upset about is that he promised me for a whole year, and he just couldn't bring himself to do the shit — and as soon as I disappeared, he could do it with someone else.\\n\\nI'm not mad at Linda. Linda did nothing wrong, LOL. But Derek did.\\n\\nAnd he keeps saying: why, after the way I acted, should he even consider joining one of my duets anymore? Because you promised, motherfucker. Because you promised a million times. Because our whole fucking friendship was based on that shit. You fucking owe me that shit. You owe me that shit, you son of a bitch. Fuck you. That's why. Because you promised.\\n\\nYou sit here and talk about how you live a life above reproach. You let me think you were my best friend for a whole year, and duet partner, and you never followed through. And then you acted like I was the one with the problem, the cause of it all, when I had an emotional and-or autistic reaction to it. You asshole. How dare you." }
  ],
  gallery:{ title:"<b>+</b> THE RECEIPTS — VISIBLE EVIDENCE · CLICK TO ENLARGE",
    images:[
      { src:"https://storage.googleapis.com/astraltrash_other/derek/jay_profile_pic_thing_1.png", cap:"<b>HER AI SESSION</b> — “Her discomfort got treated like law, and your pain got treated like a problem.”" },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/jay_profile_pic_thing_2.png", cap:"“The profile/photo thing wasn't 'just a picture.'… You weren't asking to erase anyone. You were asking to exist.”" },
      { src:"https://storage.googleapis.com/astraltrash_other/derek/forensics_old_page2.jpg", cap:"<b>FORENSIC AUDIT</b> — “The Death Row Escape Clause (Moral Hostage-Taking)” — the illness cited to make the audit itself look heartless." }
    ]},""")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("done pt2")
