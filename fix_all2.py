import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# 1. Epigraphs
# Original:
#            ))}
#          </div>
#
#        <div className="relative">
# Should be:
#            ))}
#          </div>
#        )}
content = re.sub(
    r'(</cite>\s*</blockquote>\s*\)\)}\s*</div>)',
    r'\1\n        )}',
    content
)

# 2. Mechanism Map
# Original:
#            {i < parsed.mechanism.length - 1 && (
#              <div className="marrow" aria-hidden="true">→</div>
#                </div>
#        ))}
# Wait, let's look at the actual code in the file.
