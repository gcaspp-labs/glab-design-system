# Changelog

## 2.0.0 — 2026-11-24

Mudança de marca: o polvo (mascote provisório da GCASPP LAB) dá lugar ao logo GCASPP modernizado.

- Logo GCASPP redesenhado: anel e três barras em uma cor só, com folgas vazadas, sem sombra e sem serifa. O texto é IBM Plex Sans 600, convertido em curvas.
- Novos em `assets/logos/`: `gcaspp-horizontal(-escuro).svg`, `gcaspp-vertical(-escuro).svg`, `gcaspp-simbolo.svg`, `-escuro`, `-ink` e `-branco`.
- Novo `assets/logos/favicon/`: `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` e `site.webmanifest`, com um símbolo reforçado para tamanhos pequenos.
- **Removidos** (quebra compatibilidade): `glab-simbolo*.svg`, `gcaspp-lab-horizontal*.svg` e `g-lab*.svg`. Troca:

  | Antes | Agora |
  |---|---|
  | `glab-simbolo.svg` | `gcaspp-simbolo.svg` (favicon: `favicon/favicon.svg`) |
  | `glab-simbolo-escuro.svg` | `gcaspp-simbolo-escuro.svg` |
  | `glab-simbolo-ink.svg` | `gcaspp-simbolo-ink.svg` |
  | `glab-simbolo-branco.svg` | `gcaspp-simbolo-branco.svg` |
  | `gcaspp-lab-horizontal.svg` | `gcaspp-horizontal.svg` |
  | `gcaspp-lab-horizontal-escuro.svg` | `gcaspp-horizontal-escuro.svg` |
  | `g-lab.svg` / `g-lab-escuro.svg` | `gcaspp-horizontal.svg` / `gcaspp-horizontal-escuro.svg` |

- A marca na interface passa a ser "GCASPP"; "g-lab" fica só para repositórios, pacotes e URLs. O brand book ("Nome e marca") e o Sidebar foram atualizados.
- `.brand-mark` agora tem altura fixa de 32px e largura automática, porque o símbolo novo é mais largo que alto.
- Sem mudança: tokens, fontes e os demais componentes.

## 1.1.0 — 2026-11-18

- Cores trocadas para o padrão da GCASPP, tiradas do logo: azul-marinho `#01466F` (`accent` do claro), azul claro `#4BAECE` (`accent` do escuro) e cinzas neutros, sem matiz azul (superfícies, bordas, textos e `sidebar-*`).
- Tokens alterados: `ink`, `ink-soft`, `ink-faint`, `paper`, `surface`, `surface-2`, `line`, `line-soft`, `accent`, `accent-strong`, `accent-soft`, `on-accent` e `sidebar-*`, nos temas claro e escuro. Os contrastes citados nas descrições foram recalculados.
- Sem mudança: `success`, `warning`, `danger` (e `-soft`/`-ink`), `overlay`, `shadow`, espaçamentos, raios, fontes e componentes.
- Logos em `assets/logos` com as cores novas, mesmo desenho: `#1F5E63`→`#01466F`, `#1B2430`→`#222222`, `#5FB4B8`→`#4BAECE`, `#8AD0D3`→`#86CBE2`, `#E7EBE9`→`#EBEBEB`.

## 1.0.0 — 2026-10-24

- Primeira versão, extraída do sistema Contratos GCASPP.
- Logo GCASPP LAB (polvo) nas cores do sistema: símbolo, assinatura horizontal e g-lab, para fundo claro e escuro.
- Tokens de cor (claro/escuro), tipografia IBM Plex, espaçamento, raio, sombra e layout.
- 19 componentes em CSS puro com diretrizes e exemplos.
