import re
with open("src/data/modules.ts", "r") as f:
    content = f.read()

content = content.replace("'{ title: '\"BUT I'M YOUR DUET PARTNER\"',", "{ title: '\"BUT I\\'M YOUR DUET PARTNER\"',")
content = content.replace("{ title: '\"BUT I'M YOUR DUET PARTNER\"',", "{ title: '\"BUT I\\'M YOUR DUET PARTNER\"',")
content = content.replace("{ title: '\"BUT I\\'M YOUR DUET PARTNER\"',", "{ title: \"\\\"BUT I'M YOUR DUET PARTNER\\\"\",")

with open("src/data/modules.ts", "w") as f:
    f.write(content)
print("fixed single quote in addendum")
