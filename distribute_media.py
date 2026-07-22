import re
import json

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Define the replacements as a list of tuples: (pattern_to_match, replacement_with_media)

replacements = [
    # Module 02
    (
        r'name:"The “Complex” as a Shield",\s*ids:\[\["TESTIMONY"\],\["STARMAKER"\],\["WA-1135","12/29/25"\],\["WA-1494","01/22/26"\]\],',
        r'name:"The “Complex” as a Shield",\n        media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/his_complex_he_quits.mp4" },\n        ids:[["TESTIMONY"],["STARMAKER"],["WA-1135","12/29/25"],["WA-1494","01/22/26"]],'
    ),
    (
        r'name:"The Final Dissolution — withdrawal as “delivering my conquered complex”",\s*ids:\[\["WA-1906","02/16/26 2:31 AM"\]\],',
        r'name:"The Final Dissolution — withdrawal as “delivering my conquered complex”",\n        media: { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/complex_quits2.mp4" },\n        ids:[["WA-1906","02/16/26 2:31 AM"]],'
    ),
    (
        r'name:"The Condition Appears",\s*ids:\[\["WA-0560","12/12/25 9:09 AM"\],\["SC-28","the hand-circled page"\]\],',
        r'name:"The Condition Appears",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/requesting time to hang out.PNG" },\n        ids:[["WA-0560","12/12/25 9:09 AM"],["SC-28","the hand-circled page"]],'
    ),
    (
        r'name:"The Unprompted Offer",\s*ids:\[\["WA-0241","12/08/25 2:55 PM"\]\],',
        r'name:"The Unprompted Offer",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/video_call_promise.jpg" },\n        ids:[["WA-0241","12/08/25 2:55 PM"]],'
    ),
    # Module 04: Gaslighting - let's add them to the mechanisms and exhibits
    (
        r'name:"The Past-Tense Confession — “I\'m wrong 100%” \(terms & conditions apply\)",\s*ids:\[\["WA-1879","02/16/26 2:17 AM"\]\],',
        r'name:"The Past-Tense Confession — “I\'m wrong 100%” (terms & conditions apply)",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/gaslighting_pain_level15.PNG" },\n        ids:[["WA-1879","02/16/26 2:17 AM"]],'
    ),
    (
        r'name:"“The guilt game” — present and future declared negotiable",\s*ids:\[\["WA-1885","02/16/26 2:24 AM"\]\],',
        r'name:"“The guilt game” — present and future declared negotiable",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/gaslighting222.PNG" },\n        ids:[["WA-1885","02/16/26 2:24 AM"]],'
    ),
    (
        r'name:"The Debt Inverted — her trust is why he broke it",\s*ids:\[\["WA-1891","02/16/26 2:27 AM"\]\],',
        r'name:"The Debt Inverted — her trust is why he broke it",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/complex_gaslighting.PNG" },\n        ids:[["WA-1891","02/16/26 2:27 AM"]],'
    ),
    (
        r'name:"The Perspective Guy — the self-appointed reality editor",\s*ids:\[\["WA-1903","02/16/26 2:29 AM"\],\["WA-0366","12/09/25"\]\],',
        r'name:"The Perspective Guy — the self-appointed reality editor",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/gaslighting_complex333.PNG" },\n        ids:[["WA-1903","02/16/26 2:29 AM"],["WA-0366","12/09/25"]],'
    ),
    (
        r'name:"The Martyr Withdrawal",\s*ids:\[\["WA-1906","02/16/26 2:31 AM"\]\],',
        r'name:"The Martyr Withdrawal",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/gaslighting_fuckhim.PNG" },\n        ids:[["WA-1906","02/16/26 2:31 AM"]],'
    ),
    (
        r'name:"The Diagnostic Smear — “you suck, Merry”",\s*ids:\[\["WA-1975","02/16/26 3:52 AM"\]\],',
        r'name:"The Diagnostic Smear — “you suck, Merry”",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/gaslighting_narcissism.PNG" },\n        ids:[["WA-1975","02/16/26 3:52 AM"]],'
    ),
    # Add face requirement to The Auditory Processing Blockade
    (
        r'name:"The Auditory Processing Blockade",\s*ids:\[\["TESTIMONY"\],\["WA-1688"\],\["WA-0790"\]\],',
        r'name:"The Auditory Processing Blockade",\n        media: { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/face_request.jpg" },\n        ids:[["TESTIMONY"],["WA-1688"],["WA-0790"]],'
    )
]

for pat, rep in replacements:
    content = re.sub(pat, rep, content)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
