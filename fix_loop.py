with open("src/pages/ModulePage.tsx", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<div className="mloop"' in line:
        lines.insert(i+1, '        )}\n')
        break

with open("src/pages/ModulePage.tsx", "w") as f:
    f.writelines(lines)
