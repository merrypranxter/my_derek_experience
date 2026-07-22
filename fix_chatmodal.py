with open("src/components/ChatModal.tsx", "r") as f:
    content = f.read()

content = content.replace("  if (!chatId) return null;\n\n  return (\n    <AnimatePresence>\n      <motion.div", "  return (\n    <AnimatePresence>\n      {chatId && (\n      <motion.div")
content = content.replace("        </motion.div>\n      </motion.div>\n    </AnimatePresence>\n  );\n}", "        </motion.div>\n      </motion.div>\n      )}\n    </AnimatePresence>\n  );\n}")

with open("src/components/ChatModal.tsx", "w") as f:
    f.write(content)
