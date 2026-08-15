# Exercício 4 — Complete a tabela de complexidade (gabarito)

| Operação | Contígua | Por quê? | Encadeada | Por quê? |
|---|---|---|---|---|
| Acesso por índice | **O(1)** | o endereço do elemento é calculado direto (`base + índice × tamanho_do_elemento`), sem precisar percorrer nada | **O(n)** | não existe acesso direto por posição; é preciso percorrer nó a nó a partir do início até chegar lá |
| Inserir no início | **O(n)** | todo o conteúdo existente precisa deslocar uma posição para abrir espaço na posição 0 | **O(1)** | basta criar o novo nó e apontar seu `proximo` para o antigo início — nada mais se move |
| Inserir no fim | **O(1) amortizado** | se há espaço livre, grava direto na próxima posição; só ocasionalmente precisa realocar para um array maior | **O(1)** | com um ponteiro para o último nó mantido pela própria lista, basta religar esse ponteiro — sem ele, seria O(n) |
| Buscar por valor | **O(n)** | no pior caso (valor no fim, ou ausente), é preciso examinar elemento por elemento | **O(n)** | mesma lógica: sem atalho, é preciso percorrer nó a nó até encontrar ou chegar ao fim |

## O ponto central

Repare que **buscar por valor é O(n) nas duas estruturas** — a
diferença entre elas não está em "qual é mais rápida" de forma
absoluta, mas em **qual operação cada uma favorece**. A contígua
favorece acesso por posição; a encadeada favorece inserção/remoção nas
pontas. Escolher a estrutura certa depende de qual operação seu
problema faz com mais frequência.
