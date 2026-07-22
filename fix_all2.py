import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

# Replace }; MODULE_DATA['XX'] = { with }, 'XX': {
content = re.sub(r'\s*\};\s*MODULE_DATA\[\'(\d+)\'\] = \{', r'\n  },\n  \'\1\': {', content)

# And make sure the file ends with a proper object closure
# First remove all trailing }; or }
content = re.sub(r'[\s\}]+;?$', '', content)
# Then append the proper closing
content += '\n  }\n};\n'

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed all objects to be inside one object")
