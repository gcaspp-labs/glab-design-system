# Logos

Marca GCASPP: anel com três barras. Todos os arquivos são SVG com uma cor só e o texto convertido em curvas, então não dependem de fonte instalada. As folgas entre as barras e o anel são vazadas e mostram o fundo.

## Assinaturas

- `gcaspp-horizontal.svg`: símbolo em `accent` (#01466F) + "GCASPP" (IBM Plex Sans 600, `ink` #222222). É a assinatura principal, para cabeçalhos, login, documentos e site.
- `gcaspp-horizontal-escuro.svg`: a mesma assinatura para fundos escuros: símbolo em #4BAECE e texto em #EBEBEB.
- `gcaspp-vertical.svg` / `gcaspp-vertical-escuro.svg`: símbolo sobre o texto, para capas, telas de abertura e espaços quadrados.

## Símbolo

- `gcaspp-simbolo.svg`: em `accent` claro (#01466F), para fundos claros e avatar.
- `gcaspp-simbolo-escuro.svg`: em `accent` escuro (#4BAECE), para a barra lateral e o tema escuro.
- `gcaspp-simbolo-ink.svg`: em `ink` (#222222), para impressão monocromática e carimbos.
- `gcaspp-simbolo-branco.svg`: em branco, sobre fotos ou cores sólidas escuras.

O símbolo é mais largo que alto (cerca de 1,15:1). Fixe a altura e deixe a largura automática.

## Favicon e ícones (`favicon/`)

Os ícones usam uma versão reforçada do símbolo, com anel mais grosso e folgas maiores, para ficar legível a 16px. O símbolo aparece em branco sobre um quadrado `accent`.

- `favicon.svg`, `favicon.ico` (16, 32 e 48px)
- `apple-touch-icon.png` (180px)
- `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` (Android/PWA)
- `site.webmanifest`

Copie os arquivos para a raiz pública do sistema (`public/`) e adicione no `<head>`:

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#01466F">
```

No `site.webmanifest`, troque `name` e `short_name` pelo nome do sistema.

## Regras

- Tamanho mínimo do símbolo: 24px de altura. Abaixo disso, use o favicon.
- Deixe em volta um espaço livre de metade da altura do símbolo.
- Não gire, não contorne e não aplique sombra nem degradê. As partes vazadas nunca recebem outra cor.
- Não separe o símbolo do texto nem mude a proporção entre eles nas assinaturas.
