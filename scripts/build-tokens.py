#!/usr/bin/env python3
"""Gera tokens/tokens.css a partir de tokens/tokens.json.

Uso: python3 scripts/build-tokens.py
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
t = json.loads((ROOT / "tokens/tokens.json").read_text(encoding="utf-8"))


def alias(v):
    return re.sub(r"\{([^}]+)\}", r"var(--\1)", v)


def colors(theme, indent="  "):
    out = []
    for k in t["color"]["tokens"]:
        v = k["value"]
        v = v.get(theme, v["light"]) if isinstance(v, dict) else v
        out.append(f"{indent}--{k['name']}: {alias(v)};")
    for k in t.get("shadow", {}).get("tokens", []):
        v = k["value"]
        v = v.get(theme, v["light"]) if isinstance(v, dict) else v
        out.append(f"{indent}--{k['name']}: {v};")
    return "\n".join(out)


static = []
for fam in ("spacing", "radius", "layout"):
    for k in t.get(fam, {}).get("tokens", []):
        static.append(f"  --{k['name']}: {k['value']};")
for key, stack in t["type"]["families"].items():
    static.append(f"  --font-{key}: {stack};")

styles = []
for g in t["type"]["groups"]:
    for s in g["styles"]:
        fam = s.get("family", g["family"])
        rules = [
            f"font-family: var(--font-{fam})",
            f"font-size: {s['fontSize']}",
            f"line-height: {s['lineHeight']}",
            f"font-weight: {s['fontWeight']}",
        ]
        if "letterSpacing" in s:
            rules += [f"letter-spacing: {s['letterSpacing']}", "text-transform: uppercase"]
        if fam == "mono":
            rules.append("font-variant-numeric: tabular-nums")
        styles.append(f".t-{s['name']} {{ {'; '.join(rules)}; }}")

css = f"""/* GCASPP LAB (g-lab) — gerado a partir de tokens/tokens.json. Não edite à mão: rode scripts/build-tokens.py */

/* Tema claro (padrão) */
:root, [data-theme="light"] {{
{colors("light")}
}}

/* Tema escuro: segue o sistema, a menos que data-theme="light" force o claro */
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
{colors("dark", "    ")}
  }}
}}
[data-theme="dark"] {{
{colors("dark")}
}}

:root {{
{chr(10).join(static)}
}}

/* Estilos de texto */
{chr(10).join(styles)}
"""
(ROOT / "tokens/tokens.css").write_text(css, encoding="utf-8")
print("tokens/tokens.css atualizado")
