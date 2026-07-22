import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Make sure all MODULE_DATA['XX'] = { are preceded by }; instead of being inside the object literal!
# Wait! In the original file, was it an object literal all the way through?!
