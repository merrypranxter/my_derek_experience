with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Fix intersection observer to target both .exhibit and .dsec
content = content.replace(
    "const cards = Array.from(document.querySelectorAll('.exhibit'));",
    "const cards = Array.from(document.querySelectorAll('.exhibit, .dsec'));"
)

# Fix the initial rendering of .dsec to not include 'dealt' hardcoded
content = content.replace(
    'className="dsec dealt"',
    'className="dsec"'
)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)

print("Fixed ModulePage.tsx")
