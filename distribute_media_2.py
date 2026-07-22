import re
import json

with open("src/data/modules.ts", "r") as f:
    content = f.read()

replacements = [
    # Module 06
    (
        r'name:"The Discarding of Labor",\s*ids:\[\["WA-1135","12/29/25"\],\["WA-1494","01/22/26"\],\["WA-0448","12/11/25"\]\],',
        r'name:"The Discarding of Labor",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/forensics_shadow_labor.jpeg" },\n        ids:[["WA-1135","12/29/25"],["WA-1494","01/22/26"],["WA-0448","12/11/25"]],'
    ),
    (
        r'name:"The Arithmetic of Attention",\s*ids:\[\["DATA_INDEX"\]\],',
        r'name:"The Arithmetic of Attention",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/forensics_old_page2.jpg" },\n        ids:[["DATA_INDEX"]],'
    ),
    # Module 05
    (
        r'name:"The Named Ranks",\s*ids:\[\["TESTIMONY"\],\["FORENSIC_PATTERN_ANALYSIS"\]\],',
        r'name:"The Named Ranks",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/jay_profile_pic_thing_1.png" },\n        ids:[["TESTIMONY"],["FORENSIC_PATTERN_ANALYSIS"]],'
    ),
    (
        r'name:"The Cancer Shield",\s*ids:\[\["TESTIMONY"\]\],',
        r'name:"The Cancer Shield",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/cuck1.png" },\n        ids:[["TESTIMONY"]],'
    ),
    (
        r'name:"The Flirtation Contrast",\s*ids:\[\["TESTIMONY"\],\["FORENSIC_PATTERN_ANALYSIS"\]\],',
        r'name:"The Flirtation Contrast",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/my_most_representation%20on_his_page.jpg" },\n        ids:[["TESTIMONY"],["FORENSIC_PATTERN_ANALYSIS"]],'
    ),
    # Module 01 Addendum
    (
        r'\{ title: "THE SPOT ON HIS PROFILE", text: `And it wasn\'t just about the duet',
        r'{ title: "THE SPOT ON HIS PROFILE", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/jay_profile_pic_thing_2.png" }, text: `And it wasn\'t just about the duet'
    ),
    (
        r'\{ title: "NICE FIRST", text: "And like at first I would try to talk him into it',
        r'{ title: "NICE FIRST", media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/preparing%20a%20duet%20for%20derek.jpg" }, text: "And like at first I would try to talk him into it'
    )
]

for pat, rep in replacements:
    content = re.sub(pat, rep, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
