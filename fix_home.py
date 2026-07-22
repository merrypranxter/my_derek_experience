with open("src/pages/Home.tsx", "r") as f:
    content = f.read()

target = "ref={el => chipsRef.current[i] = el}"
replacement = "ref={el => { chipsRef.current[i] = el; }}"

content = content.replace(target, replacement)

with open("src/pages/Home.tsx", "w") as f:
    f.write(content)

print("Fixed Home.tsx")
