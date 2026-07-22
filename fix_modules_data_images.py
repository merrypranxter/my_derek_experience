import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Add images to module 02 - The Withholding (or wherever appropriate)
target = """        ids:[["WA-1135","12/29/25 9:53 PM"],["WA-1494","01/22/26 1:17 AM"],["WA-1496","voice, 7 min"],["WA-1499","voice, 39 min"]],"""
replacement = """        ids:[["WA-1135","12/29/25 9:53 PM"],["WA-1494","01/22/26 1:17 AM"],["WA-1496","voice, 7 min"],["WA-1499","voice, 39 min"]],
        media: [
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_1.PNG", alt: "Duet evidence 1" },
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_2.PNG", alt: "Duet evidence 2" }
        ],"""

if target in content:
    content = content.replace(target, replacement)
    print("Added duet images to Module 03 (Capability Receipts)")

# Add art images to module 10 - The Duet Art
target2 = """      { num:"10.1", status:"ARTIFACT_RECOVERED",
        name:"The Character Designs & Worldbuilding",
        ids:[["ART-01","Initial concepts"],["ART-04","Final sprites"]],"""
replacement2 = """      { num:"10.1", status:"ARTIFACT_RECOVERED",
        name:"The Character Designs & Worldbuilding",
        ids:[["ART-01","Initial concepts"],["ART-04","Final sprites"]],
        media: [
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_1.jpeg", alt: "Art created for Derek 1" },
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_2.jpg", alt: "Art created for Derek 2" }
        ],"""

if target2 in content:
    content = content.replace(target2, replacement2)
    print("Added art images to Module 10")

with open("src/data/modules.ts", "w") as f:
    f.write(content)

