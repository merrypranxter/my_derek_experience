import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

replacements = [
    # Module 07
    (
        r'name:"The Duets With Other Women",\s*ids:\[\["TESTIMONY"\],\["STARMAKER"\],\["WA-1494","corroboration"\]\],',
        r'name:"The Duets With Other Women",\n        media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/PERFECT_duets_thisone.mp4" },\n        ids:[["TESTIMONY"],["STARMAKER"],["WA-1494","corroboration"]],'
    ),
    (
        r'name:"The Expired Deadline — the archive\'s final entry",\s*ids:\[\["WA-2063","05/18/26 10:02 AM"\],\["WA-2094","05/18/26 10:24 AM"\]\],',
        r'name:"The Expired Deadline — the archive\'s final entry",\n        media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/argument_waiting_for_apology_ga.mp4" },\n        ids:[["WA-2063","05/18/26 10:02 AM"],["WA-2094","05/18/26 10:24 AM"]],'
    ),
    (
        r'name:"The Legacy Narrative — “she\'s mad so she doesn\'t have to hate herself”",\s*ids:\[\["TESTIMONY","third-party framing"\]\],',
        r'name:"The Legacy Narrative — “she\'s mad so she doesn\'t have to hate herself”",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/gaslighting.PNG" },\n        ids:[["TESTIMONY","third-party framing"]],'
    ),
    (
        r'name:"The Gibberish Verdict",\s*ids:\[\["WA-2027–2032","05/16/26 11:32–11:45 PM"\]\],',
        r'name:"The Gibberish Verdict",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/last_words3.PNG" },\n        ids:[["WA-2027–2032","05/16/26 11:32–11:45 PM"]],'
    )
]

for pat, rep in replacements:
    content = re.sub(pat, rep, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
