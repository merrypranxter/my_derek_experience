import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

content = content.replace(
    '<video src={media.url} autoPlay loop muted playsInline className="w-full h-auto" />',
    '<video src={media.url} controls playsInline className="w-full h-auto" />'
)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
