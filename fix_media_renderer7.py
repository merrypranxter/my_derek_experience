import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """              {!ex.crossref && ex.media && ex.media.length > 0 && (
                <div className="exhibit__media" style={{marginTop: '20px'}}>"""

replacement = """              {!ex.crossref && ex.media && ex.media.length > 0 && (
                <div className="exhibit__media" style={{marginTop: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'flex-start'}}>"""

if target in content:
    content = content.replace(target, replacement)
    print("Updated renderer 7")
else:
    print("Target not found")
    
with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
