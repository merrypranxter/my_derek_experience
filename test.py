import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

target = """{ type: "image", url: "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_1.PNG", alt: "Duet evidence 1" }"""
if target in content:
    print("Found the duet 1 image")
else:
    print("Duet 1 image not found")
