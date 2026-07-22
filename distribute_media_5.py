import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

replacements = [
    (
        r'\{title:"Discard the substance, indict the style", text:"Her content \(“you broke a year of promises”\) is never answered. Her delivery \(“you said fuck you”\) becomes the entire trial."\},',
        r'{title:"Discard the substance, indict the style", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/ugh1.jpg" }, text:"Her content (“you broke a year of promises”) is never answered. Her delivery (“you said fuck you”) becomes the entire trial."},\n'
    ),
    (
        r'\{title:"Crown himself the injured party", text:"He is the one with complexes, traumas, overwhelm; she is the “facilitator of unrighteous negativity.” Offender and victim swap seats — in writing, calmly, with bullet points."\}',
        r'{title:"Crown himself the injured party", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/ugh2.jpg" }, text:"He is the one with complexes, traumas, overwhelm; she is the “facilitator of unrighteous negativity.” Offender and victim swap seats — in writing, calmly, with bullet points."}'
    ),
    (
        r'\{title:"Map the sensory requirements", text:"For a neurodivergent person, visual cues — microexpressions, lip-reading, body language — are not bonuses. They are essential data for processing human interaction."\},',
        r'{title:"Map the sensory requirements", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/face.gif" }, text:"For a neurodivergent person, visual cues — microexpressions, lip-reading, body language — are not bonuses. They are essential data for processing human interaction."},\n'
    ),
    (
        r'\{title:"Rations", text:"Occasional old photos provide just enough reward to keep the dopamine loop alive and prevent her from giving up entirely."\}',
        r'{title:"Rations", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/face2.gif" }, text:"Occasional old photos provide just enough reward to keep the dopamine loop alive and prevent her from giving up entirely."}'
    ),
    (
        r'\{title:"Nightly phone labor", text:"Hours on the phone every night, including sleeping on the phone — despite her stated \'caged animal\' sensory aversion to telephone calls. She did it anyway. That is not a preference; that is a shift."\},',
        r'{title:"Nightly phone labor", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/acknowledgemeho.jpg" }, text:"Hours on the phone every night, including sleeping on the phone — despite her stated \'caged animal\' sensory aversion to telephone calls. She did it anyway. That is not a preference; that is a shift."},\n'
    ),
    (
        r'\{title:"Reassign the villain role", text:"She is not the creditor; she is the harasser. Not the woman who waited a year; the woman who \'hates.\' Her documented grievances are redefined as symptoms."\}',
        r'{title:"Reassign the villain role", media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/leaving2.mp4" }, text:"She is not the creditor; she is the harasser. Not the woman who waited a year; the woman who \'hates.\' Her documented grievances are redefined as symptoms."}'
    )
]

for pat, rep in replacements:
    content = re.sub(pat, rep, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
