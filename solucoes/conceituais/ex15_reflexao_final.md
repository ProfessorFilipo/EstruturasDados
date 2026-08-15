# Exercício 15 — Reflexão final (gabarito)

**Cenário:** fila de atendimento — elementos são constantemente
inseridos no fim e removidos do início; acesso a uma posição aleatória
é raro.

## Resposta esperada

A **estrutura encadeada** é a mais adequada para esse cenário.

As duas operações que o cenário descreve como frequentes —
**inserir no fim** e **remover do início** — são exatamente onde as
estruturas mais se diferenciam (ver Exercício 4):

- Inserir no fim: O(1) nas duas (a contígua também é O(1) amortizado).
- **Remover do início: O(1) na encadeada, mas O(n) na contígua** —
  toda vez que alguém é atendido, a lista contígua precisaria deslocar
  *todos* os elementos restantes uma posição para trás. Numa fila com
  muita gente, isso se torna caro rapidamente.

A limitação da lista encadeada — acesso por posição em O(n) — **não
pesa neste cenário**, porque o próprio enunciado diz que esse tipo de
acesso é raro. Não faz sentido pagar o custo de uma estrutura pensada
para acesso aleatório rápido (a contígua) quando o problema não precisa
dessa característica.

## O critério geral por trás dessa resposta

Não existe estrutura "melhor" no abstrato — existe estrutura mais
adequada **ao padrão de uso**. A pergunta certa não é "qual é mais
rápida", e sim: **quais operações este problema específico faz com
mais frequência, e qual estrutura é O(1) justamente nessas
operações?**
