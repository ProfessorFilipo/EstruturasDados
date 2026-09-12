/*
 * lista_encadeada.h
 *
 * Estruturas de Dados — Aula 1
 * TAD Lista implementado com nós ligados por ponteiros (estrutura
 * encadeada, lista simplesmente encadeada).
 *
 * Convenção de retorno das funções que podem falhar (inserir, remover,
 * obter): 1 = sucesso, 0 = falha (posição inválida ou memória insuficiente).
 */
#ifndef LISTA_ENCADEADA_H
#define LISTA_ENCADEADA_H

typedef struct No {
    int valor;
    struct No *proximo;
} No;

typedef struct {
    No *inicio;
    No *fim;     /* mantido para permitir inserir_fim em O(1) */
    int tamanho;
} ListaEncadeada;

/* Inicializa a lista (vazia). Chamar antes de qualquer outra operação. */
void lista_criar(ListaEncadeada *lista);

/* Insere 'valor' na posição 'pos' (0 <= pos <= tamanho). Custo: O(n) no
 * pior caso (é preciso percorrer até a posição anterior). */
int lista_inserir(ListaEncadeada *lista, int pos, int valor);

/* Atalhos comuns, construídos sobre a mesma lógica de lista_inserir(). */
int lista_inserir_inicio(ListaEncadeada *lista, int valor); /* O(1) */
int lista_inserir_fim(ListaEncadeada *lista, int valor);    /* O(1), graças ao ponteiro 'fim' */

/* Remove o elemento da posição 'pos'. Se 'valor_removido' não for NULL,
 * recebe o valor removido. Custo: O(n) (é preciso alcançar a posição). */
int lista_remover(ListaEncadeada *lista, int pos, int *valor_removido);

/* Retorna o índice da primeira ocorrência de 'valor', ou -1 se não
 * encontrado. Custo: O(n). */
int lista_buscar(const ListaEncadeada *lista, int valor);

/* Lê o valor da posição 'pos' em '*valor'. Custo: O(n). */
int lista_obter(const ListaEncadeada *lista, int pos, int *valor);

/* Retorna a quantidade de elementos armazenados. Custo: O(1). */
int lista_tamanho(const ListaEncadeada *lista);

/* Imprime todos os elementos, na ordem, um por linha. Custo: O(n). */
void lista_percorrer(const ListaEncadeada *lista);

/* Libera todos os nós alocados dinamicamente. Chamar ao final do uso da
 * lista para não vazar memória (não existe coletor de lixo em C!). */
void lista_destruir(ListaEncadeada *lista);

#endif /* LISTA_ENCADEADA_H */
