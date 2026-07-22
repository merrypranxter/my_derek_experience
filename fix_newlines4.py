with open("src/data/modules.ts", "r") as f:
    orig = f.read()

import re
orig = re.sub(r'A man living “above reproach” does not issue threats against his own chat history.*?The plea is the confession\."', r'A man living “above reproach” does not issue threats against his own chat history.\\n\\nThe plea is the confession."', orig, flags=re.DOTALL)

with open("src/data/modules.ts", "w") as f:
    f.write(orig)
