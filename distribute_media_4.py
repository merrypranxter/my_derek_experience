import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

replacements = [
    (
        r'\{title:"Bait the reaction", text:"Withhold, disappear, move the goalpost \(Modules 2–3\) until the victim — autistic, sleep-deprived from phone labor, a year into broken promises — reacts with volume."\},',
        r'{title:"Bait the reaction", media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/near_the_end_im_fed_up.mp4" }, text:"Withhold, disappear, move the goalpost (Modules 2–3) until the victim — autistic, sleep-deprived from phone labor, a year into broken promises — reacts with volume."},\n'
    ),
    (
        r'\{title:"Restrict the channel", text:"Communication is confined to audio-only, muffled, thick-accented calls — effectively blindfolding her social intuition and forcing total reliance on his verbal framing of reality."\},',
        r'{title:"Restrict the channel", media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/face_ultimatum_after_thanksgiving_promise.mp4" }, text:"Communication is confined to audio-only, muffled, thick-accented calls — effectively blindfolding her social intuition and forcing total reliance on his verbal framing of reality."},\n'
    )
]

for pat, rep in replacements:
    content = re.sub(pat, rep, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
