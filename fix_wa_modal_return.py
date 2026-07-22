import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Add modal to return
target = """      </nav>
    </div>
  );
}"""

replacement = """      </nav>
      <ChatModal chatId={activeChatId} onClose={() => setActiveChatId(null)} />
    </div>
  );
}"""

content = content.replace(target, replacement)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
