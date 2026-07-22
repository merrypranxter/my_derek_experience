import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Replace the wrong googleapis bucket urls with the correct public unauthenticated versions
# The console urls the user gave us won't work either because they require authentication.
content = content.replace("https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_1.PNG", "/duet_dates_1.PNG")
content = content.replace("https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_2.PNG", "/duet_dates_2.PNG")
content = content.replace("https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_1.jpeg", "/art_for_him_1.jpeg")
content = content.replace("https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_2.jpg", "/art_for_him_2.jpg")

print("Replaced storage URLs with local placeholders for the user to upload files into")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
