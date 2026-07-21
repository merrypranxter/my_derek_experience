import re

with open('src/index.css', 'r') as f:
    content = f.read()

# Replace .docket
content = re.sub(r'\.docket \{[^}]+\}', """.docket{
  position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  z-index:2;text-align:center;max-width:62%;
  pointer-events:none;
}
.docket .subject,.docket a{pointer-events:auto;}""", content)

# Replace .orbit
content = re.sub(r'\.orbit \{[^}]+\}', """.orbit{
  position:relative;
  width:min(96vw, 1200px);
  height:min(88vh, 820px);
  list-style:none;margin:0;padding:0;
}""", content)

# Replace .docket__inner if it exists
content = re.sub(r'\.docket__inner \{[^}]+\}', "", content)

# Replace media queries
mq_replacement = """@media (max-width: 719px){
  .orbit{width:100%;height:auto;display:block;}
  .orbit__ring{display:none;}
  .docket{position:static;transform:none;max-width:100%;margin:0 auto 2.5rem;pointer-events:auto;}
  .chip{position:static;display:flex;justify-content:center;margin-bottom:.6rem;}
  .chip button{transform:none;}
}"""

# Remove old media max-width 719px
content = re.sub(r'@media \(max-width: 719px\)\s*\{[^\}]+\}\s*\}', mq_replacement, content, flags=re.MULTILINE|re.DOTALL)

with open('src/index.css', 'w') as f:
    f.write(content)
