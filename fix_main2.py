with open("src/main.tsx", "r") as f:
    content = f.read()

if "ErrorBoundary" not in content[:300]:
    content = content.replace("import App from './App.tsx';", "import App from './App.tsx';\nimport { ErrorBoundary } from './ErrorBoundary';")

with open("src/main.tsx", "w") as f:
    f.write(content)
