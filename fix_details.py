with open("src/pages/ModulePage.tsx", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '</details>' in line:
        if 'className="exhibits"' in lines[i+1]:
            lines.insert(i+1, '      )}\n')
            break

with open("src/pages/ModulePage.tsx", "w") as f:
    f.writelines(lines)
