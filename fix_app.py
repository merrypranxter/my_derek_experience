with open("src/App.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'import ChatLog from "./pages/ChatLog";',
    'import ChatLog from "./pages/ChatLog";\nimport Legalities from "./pages/Legalities";'
)

content = content.replace(
    '<Route path="/chat" element={<ChatLog />} />',
    '<Route path="/chat" element={<ChatLog />} />\n            <Route path="/legalities" element={<Legalities />} />'
)

content = content.replace(
    'Visible Evidence ↗\n    </Link>\n  );',
    """Visible Evidence ↗
    </Link>
    <Link
      to="/legalities"
      className="fixed bottom-6 right-6 z-[100] opacity-30 hover:opacity-100 transition-opacity"
      style={{
        fontFamily: "var(--font-data)",
        fontSize: ".6rem",
        letterSpacing: ".2em",
        textTransform: "uppercase",
        color: "#fff",
        textDecoration: "none"
      }}
    >
      LEGALITIES
    </Link>
    </>
  );"""
)

content = content.replace(
    'return (\n    <Link',
    'return (\n    <>\n    <Link'
)

with open("src/App.tsx", "w") as f:
    f.write(content)
