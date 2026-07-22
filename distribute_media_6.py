import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

replacements = [
    (
        r'name:"The Retroactive Reclassification",\s*ids:\[\["WA-1891","02/16/26 2:27 AM"\]\],',
        r'name:"The Retroactive Reclassification",\n        media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/leaving5.mp4" },\n        ids:[["WA-1891","02/16/26 2:27 AM"]],'
    ),
    (
        r'\{title:"Replace the function publicly", text:"The thing Merry was promised for a year — on-camera duet partnership — begins happening with other women, on the same platform where the promise was born, where she can see it."\},',
        r'{title:"Replace the function publicly", media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/leaving6.mp4" }, text:"The thing Merry was promised for a year — on-camera duet partnership — begins happening with other women, on the same platform where the promise was born, where she can see it."},\n'
    )
]

for pat, rep in replacements:
    content = re.sub(pat, rep, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
