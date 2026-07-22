import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

target = """      { num:"3.6", status:"CAPABILITY_RECEIPT",
        name:"The Capability Receipts — TWO video calls after a year of “the complex”",
        ids:[["WA-1135","12/29/25 9:53 PM"],["WA-1494","01/22/26 1:17 AM"],["WA-1496","voice, 7 min"],["WA-1499","voice, 39 min"]],
        quote:"Video call, 1 hr  —  system record WA-1135\\nVideo call, 55 min —  system record WA-1494",
        note:"After a full year in which a video call was structurally impossible due to “the complex” — and just 17 days after the Dec 12 speeches in which the call would only happen “when it doesn't feel like this” (WA-0560) and would in fact “never happen between us” (WA-0605) — Derek gets on a one-hour video call. Then, mid-January-thaw, a second one at 1 AM.",
        analysis:"The single most corrosive fact for the “complex” narrative — twice over. The barrier was never capability; it was leverage. The calls happened when they cost him nothing and bought maximum goodwill — and could be withheld again the moment each thaw ended. Which they were." }"""

replacement = """      { num:"3.6", status:"CAPABILITY_RECEIPT",
        name:"The Capability Receipts — TWO video calls after a year of “the complex”",
        ids:[["WA-1135","12/29/25 9:53 PM"],["WA-1494","01/22/26 1:17 AM"],["WA-1496","voice, 7 min"],["WA-1499","voice, 39 min"]],
        quote:"Video call, 1 hr  —  system record WA-1135\\nVideo call, 55 min —  system record WA-1494",
        note:"After a full year in which a video call was structurally impossible due to “the complex” — and just 17 days after the Dec 12 speeches in which the call would only happen “when it doesn't feel like this” (WA-0560) and would in fact “never happen between us” (WA-0605) — Derek gets on a one-hour video call. Then, mid-January-thaw, a second one at 1 AM. Crucially, the Operative notes that on both of these calls, she was the only one on camera showing him her world. His screen remained completely off.",
        analysis:"The single most corrosive fact for the “complex” narrative — twice over, but with the asymmetry rigorously enforced. The barrier was never capability; it was leverage. Even when conceding the format, the one-way mirror remained intact: her visibility against his darkness. The calls happened when they cost him nothing, bought maximum goodwill, and could be withheld again the moment each thaw ended. Which they were." }"""

if target in content:
    content = content.replace(target, replacement)
    with open("src/data/modules.ts", "w") as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Target not found. Doing regex fallback...")
    
