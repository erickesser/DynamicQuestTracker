# Dynamic Quest Tracker

Um tracker dinâmico para quests do Old School RuneScape (OSRS), baseado no Wise Old Man API. Permite configurar qualquer quest principal e suas pré-requisitos para acompanhar o progresso.

## Funcionalidades

- **Configuração Dinâmica:** Use o `setup.py` para configurar a quest principal, quests diretas e secundárias.
- **Acompanhamento de Quests:** Marque quests como concluídas e veja o progresso.
- **Acompanhamento de Skills:** Atualize níveis de habilidades automaticamente via Wise Old Man API.
- **Guia de Progressão:** Veja um guia sugerido para completar a quest.
- **Resumo:** Visualize o progresso geral em uma aba de resumo.
- **Configurações:** Altere o nome do jogador no Wise Old Man.

## Como Usar

1. **Configuração Inicial:**
   ```
   python setup.py
   ```
   - Digite o nome da quest principal (ex: Dragon Slayer II).
   - Liste as quests diretas (separadas por vírgula).
   - Liste as quests secundárias (separadas por vírgula).

2. **Executar o Tracker:**
   ```
   python main.py
   ```

3. **Atualizar Skills:**
   - Na aba "⚔️ Skills", clique em "Atualizar Níveis (Wise Old Man)".
   - Certifique-se de que o nome do jogador está correto na aba "Configurações".

## Dependências

- Python 3.x
- tkinter (incluído no Python padrão)
- requests

Instale requests se necessário:
```
pip install requests
```

## Estrutura do Projeto

- `main.py`: Ponto de entrada principal da aplicação.
- `setup.py`: Script de configuração inicial.
- `skills/`: Módulo para acompanhar níveis de habilidades.
- `quests/`: Módulo para acompanhar quests diretas.
- `chain/`: Módulo para acompanhar quests secundárias.
- `summary/`: Módulo para resumo do progresso.
- `config/`: Módulo para configurações.
- `guide/`: Módulo para guia de progressão.
- `utils/`: Utilitários, incluindo funções para API e dados.

## API Wise Old Man

O projeto usa a API do Wise Old Man para buscar dados de habilidades. Certifique-se de que o nome do jogador está registrado no Wise Old Man.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou relatar bugs.

## Licença

Este projeto é de código aberto. Use e modifique como quiser.
