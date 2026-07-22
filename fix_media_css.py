with open("src/module.css", "a") as f:
    f.write("\n.exhibit__media {\n  margin-top: 1.5rem;\n}\n.exhibit__media .img-wrap {\n  border: 1px solid var(--atm-dim);\n  padding: 5px;\n  background: rgba(0,0,0,0.2);\n  transition: all 0.2s ease;\n}\n.exhibit__media .img-wrap:hover {\n  border-color: var(--atm-cyan);\n  background: rgba(0,0,0,0.5);\n}\n")
print("CSS updated")
