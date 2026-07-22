import re

with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

target = "an archive in thirteen modules. the record does not change."
if target in content:
    print("It is already thirteen")
else:
    print("Not thirteen")
