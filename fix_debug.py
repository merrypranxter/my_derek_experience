with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

content = content.replace("export default function ModulePage() {", "export default function ModulePage() {\n  console.log('MODULE_DATA keys:', Object.keys(MODULE_DATA));")
content = content.replace("setParsed(MODULE_DATA[id]);", "console.log('Setting parsed:', MODULE_DATA[id]);\n    setParsed(MODULE_DATA[id]);")

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
