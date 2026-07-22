with open("src/components/ChatModal.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'className="fixed inset-0 z-[200]',
    'key="chat-modal"\n        className="fixed inset-0 z-[200]'
)

with open("src/components/ChatModal.tsx", "w") as f:
    f.write(content)
