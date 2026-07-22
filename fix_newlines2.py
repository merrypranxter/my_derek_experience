with open("src/data/modules.ts", "r") as f:
    orig = f.read()

import re
orig = orig.replace('history.\nThe plea', 'history.\\n\\nThe plea')
orig = orig.replace('history.\\nThe plea', 'history.\\n\\nThe plea')
with open("src/data/modules.ts", "w") as f:
    f.write(orig)
