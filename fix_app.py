import re

with open("src/App.tsx", "r") as f:
    content = f.read()

import_target = 'import VisualEvidence from "./pages/VisualEvidence";'
import_replacement = 'import VisualEvidence from "./pages/VisualEvidence";\nimport ChatLog from "./pages/ChatLog";'

route_target = '<Route path="/evidence" element={<VisualEvidence />} />'
route_replacement = '<Route path="/evidence" element={<VisualEvidence />} />\n            <Route path="/chat" element={<ChatLog />} />'

if import_target in content and route_target in content:
    content = content.replace(import_target, import_replacement)
    content = content.replace(route_target, route_replacement)
    print("Replaced App.tsx")
else:
    print("Target not found in App.tsx")

with open("src/App.tsx", "w") as f:
    f.write(content)
