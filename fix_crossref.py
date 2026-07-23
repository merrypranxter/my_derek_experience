with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

content = content.replace(
    '                </div>\n                                    {ex.crossref && (',
    '                </div>\n              )}\n              {ex.crossref && ('
)

content = content.replace(
    '                 </>\n                                    {!ex.crossref && (',
    '                 </>\n              )}\n              {!ex.crossref && ('
)

content = content.replace(
    '                <p className="exhibit__desc" dangerouslySetInnerHTML={{ __html: ex.desc }}></p>',
    '                <p className="exhibit__desc" dangerouslySetInnerHTML={{ __html: ex.desc }}></p>\n              )}'
)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
