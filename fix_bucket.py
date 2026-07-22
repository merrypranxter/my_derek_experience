import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = "const EVIDENCE_BUCKET = 'https://console.cloud.google.com/storage/browser/astraltrash_other/derek?project=gen-lang-client-0646349261&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))';"
replacement = "const EVIDENCE_BUCKET = '/derek_original_chat.txt.pdf';"

if target in content:
    content = content.replace(target, replacement)
    print("Replaced EVIDENCE_BUCKET")
else:
    print("Target not found")
    
with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
