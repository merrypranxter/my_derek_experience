import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

# Add import
content = content.replace('import { MODULE_DATA } from "../data/modules";', 'import { MODULE_DATA } from "../data/modules";\nimport TTSButton from "../components/TTSButton";')

# Epigraphs
content = content.replace('<blockquote key={i} className={`epigraph ${q.who === \'Derek\' ? \'him\' : \'her\'}`}>', '<blockquote key={i} className={`epigraph ${q.who === \'Derek\' ? \'him\' : \'her\'} relative`}>\n                <TTSButton text={q.text} className="absolute top-2 right-2" />')

# Objective
content = content.replace('<p className="objective">{parsed.objective}</p>', '<div className="relative"><TTSButton text={parsed.objective} className="absolute -top-4 right-0" /><p className="objective">{parsed.objective}</p></div>')

# Mechanism node
content = content.replace('<h3>{n.title}</h3>', '<h3>{n.title}</h3>\n              <TTSButton text={n.text} className="mt-2 opacity-50 hover:opacity-100" />')

# Exhibits
ex_target = """            <article key={i} className="exhibit" style={{ "--deal": dealAngle } as React.CSSProperties}>
              <div className="exhibit__top">"""
ex_replacement = """            <article key={i} className="exhibit relative" style={{ "--deal": dealAngle } as React.CSSProperties}>
              <TTSButton text={[ex.quote ? `Quote: ${ex.quote}` : '', ex.note ? `Note: ${ex.note}` : '', ex.analysis ? `Analysis: ${ex.analysis}` : '', ex.desc || ''].filter(Boolean).join('. ').replace(/<[^>]*>?/gm, '')} className="absolute top-4 right-4" />
              <div className="exhibit__top">"""
content = content.replace(ex_target, ex_replacement)

# Impact
imp_target = """      <ol className="impact">
        {parsed.impact?.map((imp: string, i: number) => ("""
imp_replacement = """      <div className="relative">
        <TTSButton text={parsed.impact?.join('. ').replace(/<[^>]*>?/gm, '')} className="absolute -top-10 right-0" />
        <ol className="impact">
          {parsed.impact?.map((imp: string, i: number) => ("""
content = content.replace(imp_target, imp_replacement)
content = content.replace('</ol>', '</ol>\n      </div>')


# Addendum
add_target = """                <section key={i} className="dsec dealt">
                  <h2>{sec.title}</h2>"""
add_replacement = """                <section key={i} className="dsec dealt relative">
                  <TTSButton text={sec.text.replace(/<[^>]*>?/gm, '')} className="absolute top-2 right-2" />
                  <h2>{sec.title}</h2>"""
content = content.replace(add_target, add_replacement)


with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
print("Patched ModulePage.tsx")
