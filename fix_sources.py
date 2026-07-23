with open("src/pages/ModulePage.tsx", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 's.meaning\n' in line or 's.meaning\r\n' in line:
        if '</span>' in lines[i+1]:
            lines.insert(i+1, '                    )}\n')
            break

with open("src/pages/ModulePage.tsx", "w") as f:
    f.writelines(lines)
