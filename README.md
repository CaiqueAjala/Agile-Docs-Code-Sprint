Atividade prática de conversor de moedas em Python com testes unitários e documentação usando Scrum
# Agile Docs & Code Sprint - Conversor de Moedas 💱

## 1. Descrição da Funcionalidade
Aplicação desenvolvida em Python para conversão de valores entre moedas pré-definidas (BRL, USD, EUR). A ferramenta permite ao usuário selecionar a moeda de origem, a moeda de destino e o valor desejado, retornando o valor convertido formatado e arredondado para duas casas decimais.

## 2. Diagrama de Fluxo
```text
[Início] ──> [Menu Principal] ──> [Seleção de Moedas]
                                         │
                                         ▼
                             [Entrada do Valor Numérico]
                                         │
                                         ▼
                             [Validação de Dados (< 0?)]
                                  │               │
                              (Invalido)       (Valido)
                                  │               │
                                  ▼               ▼
                            [Exibe Erro]   [Calcula Conversão e Arredonda]
                                                  │
                                                  ▼
                                       [Exibe Resultado Final]

Função Principia: converter_moeda(valor: float, origem: str, destino: str) -> float

Parâmetros:

valor: Montante a ser convertido (float).

origem: Código da moeda de origem (str, ex: 'BRL').

destino: Código da moeda de destino (str, ex: 'USD').

Retorno: Retorna o valor convertido arredondado em 2 casas decimais (float).

Exceções: Lança ValueError em casos de valores negativos ou moedas não suportadas.

Revisão de Código e Feedbacks (Code Review)
Pontos Positivos: Separação limpa entre a regra de negócio (conversor.py) e a interface do usuário no terminal (main.py), permitindo a escrita de testes unitários simples e diretos.

Pontos de Melhoria: Futuras versões podem integrar uma API REST externa para atualização dinâmica das taxas de câmbio em tempo real.
