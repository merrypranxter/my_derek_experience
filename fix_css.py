with open("src/module.css", "r") as f:
    content = f.read()

content = content.replace("a.eid, button.eid:hover,a.eid, button.eid:focus-visible", "a.eid:hover, button.eid:hover, a.eid:focus-visible, button.eid:focus-visible")
content = content.replace("a.eid, button.eid:hover .d,a.eid, button.eid:focus-visible .d", "a.eid:hover .d, button.eid:hover .d, a.eid:focus-visible .d, button.eid:focus-visible .d")
content = content.replace(".eid.ga.linked,a.eid, button.eid.ga:hover,a.eid, button.eid.ga:focus-visible", ".eid.ga.linked, a.eid.ga:hover, button.eid.ga:hover, a.eid.ga:focus-visible, button.eid.ga:focus-visible")
content = content.replace(".eid.ga.linked .d,a.eid, button.eid.ga:hover .d,a.eid, button.eid.ga:focus-visible .d", ".eid.ga.linked .d, a.eid.ga:hover .d, button.eid.ga:hover .d, a.eid.ga:focus-visible .d, button.eid.ga:focus-visible .d")

with open("src/module.css", "w") as f:
    f.write(content)
