# SCRABBLE2

Implementação em Python do jogo **SCRABBLE2** (variante de Scrabble) feita para a UC de Fundamentos da Programação do IST.
## Sobre o projeto

Este projeto implementa um jogo completo de Scrabble com:
- TADs bem definidos e encapsulados (Casa, Jogador, Vocabulário, Tabuleiro)
- Modo humano vs humano, humano vs IA e IA vs IA
- Três níveis de dificuldade para os agentes (FÁCIL, MÉDIO, DIFÍCIL)
- Baralhamento determinístico do saco de letras via XOR-shift + Fisher-Yates
- Validação rigorosa de jogadas, palavras e padrões no tabuleiro
- Interface por linha de comandos

### Funcionalidades implementadas
- Todas as operações dos TADs exigidas
- Distribuição inicial de 7 letras
- Troca de letras (`T`)
- Passar a vez (`P`)
- Jogar palavra (`J linha coluna direção palavra`)
- Regras especiais da primeira jogada (tem de cobrir o centro)
- Agentes que procuram as melhores jogadas possíveis segundo a amostragem do nível

## Como executar

```bash
python3 scrabble2.py
