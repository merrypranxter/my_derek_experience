import re

with open("src/data/modules.ts", "r") as f:
    content = f.read()

target = """    {title:"Nightly phone labor", text:"Hours on the phone every night, including sleeping on the phone — despite her stated 'caged animal' sensory aversion to telephone calls. She did it anyway. That is not a preference; that is a shift."},
    {title:"Morning wake-up calls", text:"An alarm-clock function performed daily, on his schedule."},
    {title:"Intimacy, freely given", text:"Shared freely — her idea, her initiative. He never asked. He did not complain. Put it that way and no other way. No transaction occurred; a gift is not a line item."},"""

replacement = """    {title:"Nightly phone labor", text:"Hours on the phone every night, including sleeping on the phone — despite her stated 'caged animal' sensory aversion to telephone calls. She did it anyway. That is not a preference; that is a shift."},
    {title:"Intimacy, freely given", text:"Shared freely — her idea, her initiative. He never asked. He did not complain. Put it that way and no other way. No transaction occurred; a gift is not a line item."},"""

if target in content:
    content = content.replace(target, replacement)
    print("Replaced mechanism")
else:
    print("Target not found")
    
with open("src/data/modules.ts", "w") as f:
    f.write(content)
