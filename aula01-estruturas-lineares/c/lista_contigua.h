/*
 * lista_contigua.h
 *
 * Estruturas de Dados — Aula 1
 * TAD Lista implementado sobre um array (estrutura contígua).
 *
 * Convenção de retorno das funções que podem falhar (inserir, remover,
 * buscar, obter): 1 = sucesso, 0 = falha (posição inválida ou lista cheia).
 */
#ifndef LISTA_CONTIGUA_H
#define LISTA_CONTIGUA_H

#define LISTA_CAPACIDADE_MAX 100

typedef struct {
    int dados[LISTA_CAPACIDADE_MAX];
    int tamanho;
} ListaContigua;

/* Inicializa a lista (tamanho = 0). Chamar antes de qualquer outra operação. */
void lista_criar(ListaContigua *lista);

/* Insere 'valor' na posição 'pos' (0 <= pos <= tamanho), deslocando os
 * elementos seguintes uma posição à frente. Custo: O(n). */
int lista_inserir(ListaContigua *lista, int pos, int valor);

/* Atalhos comuns, construídos sobre lista_inserir(). */
int lista_inserir_inicio(ListaContigua *lista, int valor); /* O(n) */
int lista_inserir_fim(ListaContigua *lista, int valor);    /* O(1) amortizado */

/* Remove o elemento da posição 'pos', deslocando os elementos seguintes
 * uma posição para trás. Se 'valor_removido' não for NULL, recebe o valor
 * removido. Custo: O(n). */
int lista_remover(ListaContigua *lista, int pos, int *valor_removido);

/* Retorna o índice da primeira ocorrência de 'valor', ou -1 se não
 * encontrado. Custo: O(n). */
int lista_buscar(const ListaContigua *lista, int valor);

/* Lê o valor da posição 'pos' em '*valor'. Custo: O(1). */
int lista_obter(const ListaContigua *lista, int pos, int *valor);

/* Retorna a quantidade de elementos armazenados. Custo: O(1). */
int lista_tamanho(const ListaContigua *lista);

/* Imprime todos os elementos, na ordem, um por linha. Custo: O(n). */
void lista_percorrer(const ListaContigua *lista);

#endif /* LISTA_CONTIGUA_H */
