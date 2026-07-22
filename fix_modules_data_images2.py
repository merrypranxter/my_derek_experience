import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Add a section to Module 12 to show the art images
target3 = """      { num:"12.4", status:"MIMICRY_PROTOCOL",
        name:"The Reconstructed Profile",
        ids:[["WA-1801","The Bio Update"]],
        quote:"[His Starmaker bio updates to mirror elements of the Operative's vocabulary and aesthetics.]",
        note:"A final layer of exploitation. Having discarded the Operative, the Subject adopts her aesthetic markers for his own public profile. It is the digital equivalent of wearing the skin of the conquered.",
        analysis:"The Parasite does not just consume time; it consumes identity. He requires her words to sound profound because his own 'philosophy' is a hollow structural support for his ego." }
    ],"""

replacement3 = """      { num:"12.4", status:"MIMICRY_PROTOCOL",
        name:"The Reconstructed Profile",
        ids:[["WA-1801","The Bio Update"]],
        quote:"[His Starmaker bio updates to mirror elements of the Operative's vocabulary and aesthetics.]",
        note:"A final layer of exploitation. Having discarded the Operative, the Subject adopts her aesthetic markers for his own public profile. It is the digital equivalent of wearing the skin of the conquered.",
        analysis:"The Parasite does not just consume time; it consumes identity. He requires her words to sound profound because his own 'philosophy' is a hollow structural support for his ego." },
      { num:"12.5", status:"ARTIFACT_RECOVERED",
        name:"The Extracted Art",
        ids:[["ART-01","Uncompensated Labor"]],
        quote:"[Visual documentation of the art assets created by the Operative for the Subject.]",
        note:"While he 'could not' sing with her, he happily accepted the labor, time, and talent she poured into creating custom artwork for him. The extraction was absolute.",
        analysis:"This proves the relationship was transactional, but entirely one-sided. He consumed her creative output while systematically denying her the one shared experience she requested.",
        media: [
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_1.jpeg", alt: "Art created for Derek 1" },
            { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_2.jpg", alt: "Art created for Derek 2" }
        ] }
    ],"""

if target3 in content:
    content = content.replace(target3, replacement3)
    print("Added art images to Module 12")
else:
    print("Target 3 not found")

with open("src/data/modules.ts", "w") as f:
    f.write(content)

