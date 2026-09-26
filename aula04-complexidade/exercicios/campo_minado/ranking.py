"""
ranking.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
ESQUELETO: complete os trechos marcados com TODO.
A solução de exemplo está em solucoes/campo_minado/.

Ranking dos melhores tempos de cada nível, guardado em um arquivo texto.

  [Aula 1] Cada ranking é uma lista contígua, mantida SEMPRE ordenada
           pelo tempo (o menor tempo na posição 0).
  [Aula 4] Inserir um recorde = um passo do Insertion Sort: coloca no fim
           e desloca para a esquerda até achar o lugar -> O(n).
           Carregar do arquivo usa o Insertion Sort completo: como o
           arquivo já é salvo ordenado, cai no MELHOR caso -> Theta(n).

Formato do arquivo (uma linha por recorde):   nivel;tempo_em_segundos;nome
Exemplo:                                      facil;42.7;Ana
"""
import os

MAXIMO_POR_NIVEL = 10

try:
    _PASTA = os.path.dirname(os.path.abspath(__file__))
except NameError:            # alguns ambientes online não definem __file__
    _PASTA = "."
ARQUIVO_PADRAO = os.path.join(_PASTA, "ranking.txt")


def inserir_ordenado(lista, recorde):
    """Insere 'recorde' (uma tupla (tempo, nome)) na lista, mantendo a
    ordem crescente de tempo. Em caso de empate, o recorde mais antigo
    fica na frente. Devolve a posição (a partir de 0) onde ele ficou.

    Faça como o laço interno do Insertion Sort: coloque o recorde no fim
    e desloque os anteriores uma posição para a direita enquanto o tempo
    deles for MAIOR que o do novo recorde.
    Custo: O(n) no pior caso (novo recorde é o melhor de todos);
    O(1) no melhor caso (novo recorde é o pior)."""
    # TODO 11: inserir mantendo a lista ordenada por tempo (um passo do Insertion Sort)
    raise NotImplementedError('TODO 11 (ranking.py): inserir mantendo a lista ordenada por tempo (um passo do Insertion Sort)')


def ordenar_por_insercao(lista):
    """Ordena a lista de recordes por tempo, no lugar, com Insertion Sort.
    É estável: empates mantêm a ordem original.
    Custo: Theta(n) se a lista já estiver ordenada (o caso do arquivo que
    nós mesmos salvamos); Theta(n^2) no pior caso."""
    # TODO 12: ordenar a lista pelo tempo usando Insertion Sort
    raise NotImplementedError('TODO 12 (ranking.py): ordenar a lista pelo tempo usando Insertion Sort')


def limpar_nome(nome):
    """Remove caracteres que quebrariam o arquivo e limita o tamanho."""
    nome = (nome or "").replace(";", " ").replace("\n", " ").replace("\r", " ").strip()
    return nome[:20] if nome else "Anonimo"


class Ranking:
    """Os melhores tempos de cada nível ("facil", "medio", "dificil")."""

    def __init__(self, caminho=ARQUIVO_PADRAO, maximo=MAXIMO_POR_NIVEL):
        self.caminho = caminho
        self.maximo = maximo
        self._por_nivel = {}          # nivel -> lista de (tempo, nome), ordenada

    def melhores(self, nivel):
        """Cópia da lista de recordes do nível, do melhor para o pior."""
        return list(self._por_nivel.get(nivel, []))

    def entraria(self, nivel, tempo):
        """True se esse tempo entraria no ranking do nível. Custo: O(1)."""
        lista = self._por_nivel.get(nivel, [])
        return len(lista) < self.maximo or tempo < lista[-1][0]

    def registrar(self, nivel, nome, tempo):
        """Registra o recorde e devolve a colocação (1 = primeiro lugar),
        ou None se o tempo não entrou entre os melhores. Custo: O(n)."""
        lista = self._por_nivel.setdefault(nivel, [])
        posicao = inserir_ordenado(lista, (round(tempo, 1), limpar_nome(nome)))
        if len(lista) > self.maximo:
            lista.pop()               # remove o pior (o último): O(1)
        return posicao + 1 if posicao < self.maximo else None

    def carregar(self):
        """Lê o arquivo, ignorando linhas com defeito. Se o arquivo não
        existir (ou não puder ser lido), começa com o ranking vazio."""
        self._por_nivel = {}
        try:
            with open(self.caminho, encoding="utf-8") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(";")
                    if len(partes) != 3:
                        continue
                    nivel, tempo, nome = partes
                    try:
                        recorde = (float(tempo), limpar_nome(nome))
                    except ValueError:
                        continue
                    self._por_nivel.setdefault(nivel, []).append(recorde)
        except OSError:
            return False
        for nivel, lista in self._por_nivel.items():
            ordenar_por_insercao(lista)         # já vem ordenada: melhor caso
            del lista[self.maximo:]
        return True

    def salvar(self):
        """Grava o ranking no arquivo. Devolve False se não conseguir
        (algumas IDEs online não permitem gravar arquivos)."""
        try:
            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                for nivel, lista in self._por_nivel.items():
                    for tempo, nome in lista:
                        arquivo.write(f"{nivel};{tempo};{nome}\n")
        except OSError:
            return False
        return True
