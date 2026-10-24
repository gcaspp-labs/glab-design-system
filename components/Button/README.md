# Button

Botões de ação da interface: primário, padrão, ghost, pequeno, destrutivo em texto, botão de ícone e link de adicionar linha.

- Use `btn btn-primary` uma vez por tela, para a ação principal ("Novo contrato", "Salvar"). Texto em `on-accent` sobre `accent`.
- `btn` (padrão) para ações secundárias; `btn-ghost` para Cancelar e ações de baixa ênfase; `btn-sm` em linhas de tabela e cabeçalhos de painel.
- `btn-danger-text` para Excluir/Remover; nunca um botão vermelho cheio.
- `icon-btn` (32×32) só com `aria-label`; hover vira `danger` porque na fonte ele remove linhas repetidas.
- `add-row-btn` abaixo de grupos repetíveis ("Adicionar parcela").
- O consumidor fornece o rótulo (verbo no infinitivo ou substantivo de ação, caixa de frase) e, opcionalmente, um ícone de 15px à esquerda.
