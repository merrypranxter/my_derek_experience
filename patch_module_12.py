import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

sidebar_media_json = """
    sidebarMedia: [
      { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/PERFECT_duets_thisone.mp4", filename: "PERFECT_duets_thisone.mp4" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet%20count.jpg", filename: "duet count.jpg" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_count.jpg", filename: "duet_count.jpg" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_count22.PNG", filename: "duet_count22.PNG" },
      { type: "video", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_count_derek_othergirls.mp4", filename: "duet_count_derek_othergirls.mp4" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_count_derek_others_2.PNG", filename: "duet_count_derek_others_2.PNG" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_count_derek_with_others.PNG", filename: "duet_count_derek_with_others.PNG" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_count_my_derek_gifs2.jpg", filename: "duet_count_my_derek_gifs2.jpg" },
      { type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duets_not_highest_count_by_far.jpg", filename: "duets_not_highest_count_by_far.jpg" }
    ],
"""

target = """  '12': {
    id:"12", code:"MODULE_12_CUCKING", title:"THE CUCKING", sub:"( The Public Display Asymmetry )","""
replacement = target + sidebar_media_json

content = content.replace(target, replacement)

with open("src/data/modules.ts", "w") as f:
    f.write(content)
