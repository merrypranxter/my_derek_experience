with open('src/index.css', 'r') as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if line.startswith('@media (max-width: 719px) {') and not skip:
        # We hit the first mobile block which is broken
        skip = True
        continue
    if skip and line.startswith('}'):
        skip = False
        continue
    if not skip:
        out.append(line)

content = "".join(out)

# Append the correct desktop and mobile rules
desktop = """
.docket {
  position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);
  z-index: 2; text-align: center; max-width: 62%;
  pointer-events: none;
}
.docket .subject, .docket a { pointer-events: auto; }
.orbit {
  position: relative;
  width: min(96vw, 1200px);
  height: min(88vh, 820px);
  list-style: none; margin: 0; padding: 0;
}
.orbit__ring {
  position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none;
}
.orbit__ring circle, .orbit__ring ellipse {
  fill: none; stroke: var(--atm-dim); stroke-opacity: .38; stroke-dasharray: 2 7;
}
.chip { position: absolute; top: 50%; left: 50%; }
.chip button {
  display: flex; align-items: center; gap: .55em;
  transform: translate(-50%, -50%) translate(var(--x, 0), var(--y, 0));
  font-family: var(--font-data); font-size: .66rem; letter-spacing: .25em; text-transform: uppercase; color: var(--atm-dim); border: 1px solid rgb(111 106 128 / .4); padding: .4rem .8rem; background: var(--atm-bg); cursor: pointer; transition: all .2s; border-radius: 4px; pointer-events: auto;
}
.chip button b { font-weight: normal; letter-spacing: .06em; color: var(--atm-red); margin-right: .5em; }
.chip button:hover, .chip button:focus { color: var(--atm-cyan); border-color: var(--atm-cyan); outline: none; }
"""

mobile = """
@media (max-width: 719px) {
  .orbit { position: static; width: 100%; height: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .6rem; }
  .orbit__ring { display: none; }
  .docket { position: static; transform: none; max-width: 100%; margin: 0 auto 2.5rem; pointer-events: auto; }
  .chip { position: static; }
  .chip button { transform: none; }
}
"""

with open('src/index.css', 'w') as f:
    f.write(content + desktop + mobile)
