import re

with open('backup_index.css', 'r') as f:
    content = f.read()

# Strip out any .docket, .orbit, .chip rules
content = re.sub(r'\.docket[^{]*{[^}]*}', '', content)
content = re.sub(r'\.orbit[^{]*{[^}]*}', '', content)
content = re.sub(r'\.chip[^{]*{[^}]*}', '', content)
content = re.sub(r'@media \(max-width: 719px\)\s*{[^}]+}', '', content)

# Now just append them beautifully at the end before the last font face
rules = """
.docket { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); z-index: 2; text-align: center; max-width: 62%; pointer-events: none; }
.docket .subject, .docket a { pointer-events: auto; }
.orbit { position: relative; width: min(96vw, 1200px); height: min(88vh, 820px); list-style: none; margin: 0; padding: 0; }
.orbit__ring { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.orbit__ring ellipse { fill: none; stroke: var(--atm-dim); stroke-opacity: .38; stroke-dasharray: 2 7; }
.chip { position: absolute; top: 50%; left: 50%; }
.chip button { display: block; transform: translate(-50%, -50%) translate(var(--x, 0), var(--y, 0)); font-family: var(--font-data); font-size: .66rem; letter-spacing: .25em; text-transform: uppercase; color: var(--atm-dim); border: 1px solid rgb(111 106 128 / .4); padding: .4rem .8rem; background: var(--atm-bg); cursor: pointer; transition: all .2s; border-radius: 4px; pointer-events: auto; }
.chip button b { font-weight: normal; letter-spacing: .06em; color: var(--atm-red); margin-right: .5em; }
.chip button:hover, .chip button:focus { color: var(--atm-cyan); border-color: var(--atm-cyan); outline: none; }

@media (max-width: 719px) {
  .orbit { position: static; width: 100%; height: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .6rem; }
  .orbit__ring { display: none; }
  .docket { position: static; transform: none; max-width: 100%; margin: 0 auto 2.5rem; pointer-events: auto; }
  .chip { position: static; }
  .chip button { transform: none; }
  .exhibits::before{left:.4rem;}
  .exhibit{width:calc(100% - 2rem);margin-left:2rem !important;margin-right:0 !important;}
  .exhibit:nth-child(odd)::before,.exhibit:nth-child(even)::before{ left:calc(-2rem + .12rem);right:auto; }
  .marrow{display:none;}
}
"""

content = content + "\n" + rules
with open('src/index.css', 'w') as f:
    f.write(content)

