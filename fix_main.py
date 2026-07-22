with open("src/main.tsx", "r") as f:
    content = f.read()

content = content.replace('import App from "./App.tsx";', 'import App from "./App.tsx";\nimport { ErrorBoundary } from "./ErrorBoundary";')
content = content.replace('<App />', '<ErrorBoundary><App /></ErrorBoundary>')

with open("src/main.tsx", "w") as f:
    f.write(content)
