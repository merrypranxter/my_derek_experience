with open("src/data/modules.ts", "r") as f:
    lines = f.read().split("\n")
    for i, line in enumerate(lines[660:680]):
        print(f"{i+660}: {line}")
