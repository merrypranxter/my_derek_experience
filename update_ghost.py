import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

target = """    id:"11", code:"MODULE_11_GHOST_ANALYSIS", title:"FORENSICS", sub:"( The Deep Audit )","""
replacement = """    id:"11", code:"MODULE_11_GHOST_ANALYSIS", title:"FORENSICS", sub:"( The Deep Audit )","""

if target in content:
    content = content.replace(target, replacement)
    print("Already done")
else:
    print("Not found")

