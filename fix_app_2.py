with open("src/App.tsx", "r") as f:
    content = f.read()

target = """function GlobalStamp() {
  const location = useLocation();
  if (location.pathname !== "/") return null;
  return (
    <>
    <Link"""

replacement = """function GlobalStamp() {
  const location = useLocation();
  return (
    <>
    {location.pathname === "/" && (
      <Link"""

target2 = """Visible Evidence ↗
    </Link>
    <Link"""

replacement2 = """Visible Evidence ↗
      </Link>
    )}
    <Link"""

content = content.replace(target, replacement)
content = content.replace(target2, replacement2)

with open("src/App.tsx", "w") as f:
    f.write(content)
