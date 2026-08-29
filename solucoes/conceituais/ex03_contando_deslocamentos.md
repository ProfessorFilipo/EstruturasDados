# Exercício 3 — Contando deslocamentos (gabarito)

Lista de partida: `[10, 20, 30, 40, 50, 60]` (6 elementos, posições 0 a 5).

## 1. Inserir 99 na posição 0

- **Contígua:** desloca os **6** elementos existentes uma posição à
  frente, para abrir espaço no início.
- **Encadeada:** **0** deslocamentos. É só criar o nó novo e apontar seu
  `proximo` para o antigo `inicio` — O(1).

## 2. Inserir 99 na posição 3

- **Contígua:** desloca os **3** elementos que estão da posição 3 em
  diante (`40, 50, 60`).
- **Encadeada:** não há "deslocamento" no sentido de mover dados, mas é
  preciso **percorrer 3 nós** (posições 0, 1, 2) até alcançar o nó
  anterior à posição de inserção — o custo é proporcional a `pos`.

## 3. Inserir 99 na posição 6 (no fim)

- **Contígua:** **0** deslocamentos — insere direto na próxima posição
  livre (`pos == tamanho`).
- **Encadeada:** **O(1)**, *desde que a lista mantenha um ponteiro para
  o último nó* (como a implementação deste repositório mantém). Sem
  esse ponteiro, seria necessário percorrer os 6 nós existentes.

## 4. Remover o elemento da posição 0

- **Contígua:** desloca os **5** elementos restantes uma posição para
  trás, para preencher o buraco deixado.
- **Encadeada:** **0** deslocamentos — só reatribuir `inicio` para o
  segundo nó da lista original — O(1).

## Padrão que emerge

Na lista contígua, o custo está em **mover dados** (deslocar elementos
no array). Na lista encadeada, o custo está em **percorrer referências**
até alcançar o ponto de interesse — mas uma vez lá, a modificação em si
é sempre O(1).
