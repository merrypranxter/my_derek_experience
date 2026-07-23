with open("src/data/modules.ts", "r") as f:
    content = f.read()

# I see it swallowed Exhibit 12.6 up to its note and analysis!
bad_exhibit = """      { num:"12.5", status:"ARTIFACT_RECOVERED",
        name:"The Extracted Art",
        ids:[["ART-01","Uncompensated Labor"]],
        quote:"[Visual documentation of the art assets created by the Operative for the Subject.]",
        note:"While he 'could not' sing with her, he happily accepted the labor, time, and talent she poured into creating custom artwork for him. The extraction was absolute.",
        analysis:"This proves the relationship was transactional, but entirely one-sided. He consumed her creative output while systematically denying her the one shared experience she requested.",
        note:"“I know people were looking at me laughing. He made me look stupid to people.” — and then the reframe: “If I were the type to get embarrassed, I would be. Luckily, I'm really not. He should be embarrassed for doing that to me.”",
        analysis:"The humiliation was the public's view of the asymmetry — nothing more, nothing less. She declines the embarrassment. The record agrees with her: the shame belongs to the man who built the one-way stage on purpose, and this module is where it is filed." }"""

good_exhibit = """      { num:"12.5", status:"ARTIFACT_RECOVERED",
        name:"The Extracted Art",
        ids:[["ART-01","Uncompensated Labor"]],
        quote:"[Visual documentation of the art assets created by the Operative for the Subject.]",
        note:"While he 'could not' sing with her, he happily accepted the labor, time, and talent she poured into creating custom artwork for him. The extraction was absolute.",
        analysis:"This proves the relationship was transactional, but entirely one-sided. He consumed her creative output while systematically denying her the one shared experience she requested." },
      { num:"12.6", status:"SHAME_REASSIGNED",
        name:"The Audience Verdict",
        ids:[["TESTIMONY"]],
        note:"“I know people were looking at me laughing. He made me look stupid to people.” — and then the reframe: “If I were the type to get embarrassed, I would be. Luckily, I'm really not. He should be embarrassed for doing that to me.”",
        analysis:"The humiliation was the public's view of the asymmetry — nothing more, nothing less. She declines the embarrassment. The record agrees with her: the shame belongs to the man who built the one-way stage on purpose, and this module is where it is filed." }"""

content = content.replace(bad_exhibit, good_exhibit)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
