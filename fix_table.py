with open("src/pages/ModulePage.tsx", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<p className="ledgernote"' in line:
        if '</div>' in lines[i+1]:
            lines.insert(i+2, '      )}\n')
            break

with open("src/pages/ModulePage.tsx", "w") as f:
    f.writelines(lines)
