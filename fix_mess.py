import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# I want to remove `\n        )}` that immediately follows `          </div>`
content = content.replace("          </div>\n        )}", "          </div>")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
