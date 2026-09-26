"""
campo_minado_arquivo_unico.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado

SOLUCAO DE EXEMPLO em arquivo unico, para quem so pode usar uma IDE online.
E o mesmo codigo dos arquivos separados da pasta, juntado em um so,
sem a interface grafica (que precisa do tkinter).

Como rodar: cole tudo na IDE online (onlineide.pro/playground/python) e execute.
"""


# ======================================================================
# estruturas.py
# ======================================================================
# estruturas.py
#
# Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
# SOLUÇÃO DE EXEMPLO (este arquivo é igual ao do esqueleto).
#
# As estruturas das aulas anteriores, com a mesma interface:
#
#     Pilha     [Aula 2]  contígua: os dados ficam lado a lado em uma list
#     Fila      [Aula 2]  encadeada: nós ligados por referências (início e fim)
#     Conjunto  [Aula 3]  sem duplicatas e sem posição (sem usar o set())
#
# e um ContadorOperacoes [Aula 4], usado para medir o custo das jogadas.
#
# Regra da atividade: no núcleo do jogo (tabuleiro.py), não use set(),
# collections.deque nem queue.Queue — use só estas estruturas.
class Pilha:
    """TAD Pilha contígua com capacidade fixa. O topo é o fim da list.
    Todas as operações são O(1)."""

    def __init__(self, capacidade=20):
        self._dados = []
        self._capacidade = capacidade

    def esta_vazia(self):
        return len(self._dados) == 0

    def esta_cheia(self):
        return len(self._dados) == self._capacidade

    def tamanho(self):
        return len(self._dados)

    def empilhar(self, valor):
        if self.esta_cheia():
            raise OverflowError("pilha cheia")
        self._dados.append(valor)

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self._dados.pop()

    def consultar_topo(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self._dados[-1]

    def valores_do_topo_para_base(self):
        """Cópia dos valores, do topo para a base. Custo: O(n)."""
        return list(reversed(self._dados))


class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    """TAD Fila encadeada, com referências para o início e o fim.
    Enfileirar e desenfileirar são O(1) graças à referência 'fim'."""

    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def tamanho(self):
        return self._tamanho

    def enfileirar(self, valor):
        novo = NoFila(valor)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self._tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        removido = self.inicio
        self.inicio = removido.proximo
        if self.inicio is None:      # removeu o último nó
            self.fim = None
        self._tamanho -= 1
        return removido.valor

    def consultar_frente(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self.inicio.valor

    def valores(self):
        """Cópia dos valores, do início ao fim. Custo: O(n)."""
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado


class Conjunto:
    """TAD Conjunto sobre uma list (sem usar o set() do Python).

    pertence() percorre os elementos um a um: O(k), onde k é a
    quantidade de elementos. Se receber um ContadorOperacoes, conta
    cada comparação feita em "comparacoes_conjunto" — assim dá para
    ver no contador o custo escondido de cada consulta.
    """

    def __init__(self, contador=None):
        self._dados = []
        self._contador = contador

    def pertence(self, valor):
        """Custo: O(k). Usamos um laço explícito, e não 'valor in lista',
        para deixar visível (e contável) cada comparação."""
        for elemento in self._dados:
            if self._contador is not None:
                self._contador.incrementar("comparacoes_conjunto")
            if elemento == valor:
                return True
        return False

    def inserir(self, valor):
        """Insere se ainda não existir. Custo: O(k) por causa do pertence().
        Devolve True se inseriu, False se o valor já estava lá."""
        if self.pertence(valor):
            return False
        self._dados.append(valor)
        return True

    def remover(self, valor):
        """Remove o valor, se existir. Custo: O(k).
        Como o Conjunto não tem posição, podemos trocar o removido pelo
        último elemento e encurtar a list: não há deslocamentos."""
        for i in range(len(self._dados)):
            if self._contador is not None:
                self._contador.incrementar("comparacoes_conjunto")
            if self._dados[i] == valor:
                self._dados[i] = self._dados[-1]
                self._dados.pop()
                return True
        return False

    def tamanho(self):
        return len(self._dados)

    def valores(self):
        """Cópia dos valores (sem ordem definida). Custo: O(k)."""
        return list(self._dados)


class ContadorOperacoes:
    """Conta operações por categoria, por exemplo "celulas_visitadas".

    As categorias aparecem no relatório na ordem em que foram usadas
    pela primeira vez.
    """

    def __init__(self):
        self._contagens = {}

    def incrementar(self, nome, quantidade=1):
        self._contagens[nome] = self._contagens.get(nome, 0) + quantidade

    def registrar_maximo(self, nome, valor):
        """Guarda o maior valor já visto (ex.: tamanho máximo da fila)."""
        if valor > self._contagens.get(nome, 0):
            self._contagens[nome] = valor

    def valor(self, nome):
        return self._contagens.get(nome, 0)

    def zerar(self):
        self._contagens = {}

    def acumular(self, outro):
        """Soma as contagens de 'outro' a este contador (os máximos
        ficam com o maior valor). Usado para somar cada jogada ao total
        da partida."""
        for nome, valor in outro.itens():
            if nome.startswith("tamanho_max"):
                self.registrar_maximo(nome, valor)
            else:
                self.incrementar(nome, valor)

    def itens(self):
        return list(self._contagens.items())

    def total(self):
        return sum(v for n, v in self._contagens.items() if not n.startswith("tamanho_max"))

    def relatorio(self):
        if not self._contagens:
            return "(nenhuma operacao contada)"
        largura = max(len(nome) for nome in self._contagens)
        linhas = [f"{nome.replace('_', ' '):<{largura}}  {valor:>8}"
                  for nome, valor in self._contagens.items()]
        return "\n".join(linhas)


# ======================================================================
# tabuleiro.py
# ======================================================================
# tabuleiro.py
#
# Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
# SOLUÇÃO DE EXEMPLO. Tente primeiro o esqueleto (exercicios/campo_minado/)
# e só depois compare com esta versão.
#
# Toda a LÓGICA do jogo, sem nenhuma interface: nada de print, nada de
# janela. As interfaces (jogo_terminal.py e jogo_gui.py) apenas chamam os
# métodos públicos desta classe e desenham o resultado. Assim, a mesma
# lógica serve para as duas — e pode ser testada sozinha (testes.py).
#
# Onde cada aula aparece:
#
#   [Aula 1] O tabuleiro é guardado em LISTAS LINEARES (contíguas): a célula
#            (linha, coluna) fica na posição  linha * colunas + coluna,
#            então ler ou alterar qualquer célula custa O(1).
#   [Aula 2] FILA para abrir a área vazia em "ondas" (busca em largura);
#            PILHA para abrir em profundidade e para o histórico de jogadas.
#   [Aula 3] CONJUNTO para sortear as minas sem repetição e para as bandeiras.
#   [Aula 4] Cada método informa seu custo, e o contador de operações mede
#            o trabalho de cada jogada.
#
# Convenções:
#   - No código, linhas e colunas começam em 0. As interfaces mostram a
#     partir de 1 para o jogador.
#   - L = linhas, C = colunas, k = número de minas, f = número de bandeiras.
import random


# Deslocamentos (linha, coluna) das 8 vizinhas, NESTA ORDEM:
#   noroeste, norte, nordeste, oeste, leste, sudoeste, sul, sudeste
DIRECOES = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)

# Estados da partida
JOGANDO = "jogando"
VITORIA = "vitoria"
DERROTA = "derrota"

# O que a interface deve desenhar em cada célula (ver mapa_visivel).
# Uma célula revelada é representada pelo seu número (0 a 8).
OCULTA = "oculta"
BANDEIRA = "bandeira"
MINA = "mina"            # mina mostrada no fim da partida
EXPLODIU = "explodiu"    # a mina em que o jogador clicou
ERRO = "erro"            # bandeira colocada onde NÃO havia mina

# Níveis clássicos: (linhas, colunas, minas)
NIVEIS = {
    "facil": (9, 9, 10),
    "medio": (16, 16, 40),
    "dificil": (16, 30, 99),
}

CAPACIDADE_HISTORICO = 10_000


class Tabuleiro:
    """Estado e regras de uma partida de Campo Minado."""

    def __init__(self, linhas, colunas, num_minas, semente=None):
        if linhas < 1 or colunas < 1:
            raise ValueError("o tabuleiro precisa ter pelo menos 1 linha e 1 coluna")
        if not 0 <= num_minas < linhas * colunas:
            raise ValueError("numero de minas invalido: precisa sobrar ao menos uma celula livre")

        self.linhas = linhas
        self.colunas = colunas
        self.num_minas = num_minas
        self.total_celulas = linhas * colunas

        # [Aula 4] 'contador' mede só a jogada atual (é zerado a cada jogada);
        # 'contador_partida' acumula tudo desde o início da partida.
        self.contador = ContadorOperacoes()
        self.contador_partida = ContadorOperacoes()

        # Semente fixa -> as minas saem sempre iguais (útil para testar).
        self._gerador = random.Random(semente)

        # [Aula 1] Listas lineares com uma posição por célula: acesso O(1).
        self.numeros = [0] * self.total_celulas         # quantas minas vizinhas
        self.reveladas = [False] * self.total_celulas   # a célula já foi aberta?

        # [Aula 3] Conjuntos de índices: sem duplicatas, sem posição.
        # Eles recebem o contador para registrar cada comparação feita.
        self.minas = Conjunto(self.contador)
        self.bandeiras = Conjunto(self.contador)

        # [Aula 2] Histórico de jogadas: a mais recente fica no topo.
        # Cada jogada é uma tupla (acao, linha, coluna), com acao
        # "revelar" ou "bandeira".
        self.historico = Pilha(CAPACIDADE_HISTORICO)

        self.estrategia = "fila"          # "fila" (ondas) ou "pilha" (profundidade)
        self.estado = JOGANDO
        self.minas_posicionadas = False   # as minas só são sorteadas no 1º clique
        self.celulas_seguras_restantes = self.total_celulas - num_minas
        self.mina_explodida = None        # índice da mina clicada (derrota)

    # ------------------------------------------------------------------
    # [Aula 1] Endereçamento: (linha, coluna) <-> índice na lista linear
    # ------------------------------------------------------------------

    def indice(self, linha, coluna):
        """Posição da célula (linha, coluna) nas listas lineares.
        Exemplo, com 5 colunas: (0, 0) -> 0, (0, 4) -> 4, (1, 0) -> 5.
        Custo: O(1)."""
        # TODO 1 (resolvido): calcular o indice linear da celula (linha, coluna)
        return linha * self.colunas + coluna

    def coordenadas(self, indice):
        """Operação inversa de indice(): devolve a tupla (linha, coluna).
        Dica: use divisão inteira (//) e resto (%). Custo: O(1)."""
        # TODO 2 (resolvido): converter o indice linear de volta para (linha, coluna)
        return indice // self.colunas, indice % self.colunas

    def vizinhos(self, indice):
        """Índices das células vizinhas (até 8), na ordem de DIRECOES,
        ignorando as posições que cairiam fora do tabuleiro.
        Um canto tem 3 vizinhas; uma borda, 5; o miolo, 8.
        Custo: O(1) — no máximo 8 verificações."""
        # TODO 3 (resolvido): devolver os indices das vizinhas dentro do tabuleiro, na ordem de DIRECOES
        linha, coluna = self.coordenadas(indice)
        resultado = []
        for delta_linha, delta_coluna in DIRECOES:
            l, c = linha + delta_linha, coluna + delta_coluna
            if 0 <= l < self.linhas and 0 <= c < self.colunas:   # dentro do tabuleiro?
                resultado.append(self.indice(l, c))
        return resultado

    # ------------------------------------------------------------------
    # [Aula 3] Sorteio das minas e [Aula 4] cálculo dos números
    # ------------------------------------------------------------------

    def _posicionar_minas(self, protegida):
        """Sorteia as minas na primeira jogada, sem repetição, garantindo
        que a célula clicada ('protegida') e suas vizinhas fiquem livres
        (assim o primeiro clique sempre abre uma área). Se o tabuleiro
        for pequeno demais para proteger as vizinhas, protege só a célula.

        Conte cada tentativa de sorteio em "sorteios".
        Custo: cada inserção no Conjunto faz um pertence() O(k), então o
        sorteio todo custa cerca de O(k^2) comparações (mais as repetições).
        No fim, marca as minas como posicionadas e calcula os números."""
        # TODO 4 (resolvido): sortear num_minas indices distintos fora das celulas proibidas (use Conjunto)
        proibidas = Conjunto(self.contador)
        proibidas.inserir(protegida)
        for vizinha in self.vizinhos(protegida):
            proibidas.inserir(vizinha)
        if self.total_celulas - proibidas.tamanho() < self.num_minas:
            proibidas = Conjunto(self.contador)   # tabuleiro pequeno: protege só a clicada
            proibidas.inserir(protegida)

        while self.minas.tamanho() < self.num_minas:
            candidata = self._gerador.randrange(self.total_celulas)
            self.contador.incrementar("sorteios")
            if not proibidas.pertence(candidata):
                self.minas.inserir(candidata)     # o Conjunto ignora repetidas
        self.minas_posicionadas = True
        self._calcular_numeros()

    def definir_minas(self, indices):
        """Coloca as minas em posições escolhidas (em vez de sorteá-las).
        Usado nos testes e nos exemplos da apostila."""
        self.minas = Conjunto(self.contador)
        for i in indices:
            self.minas.inserir(i)
        if self.minas.tamanho() != self.num_minas:
            raise ValueError("a quantidade de minas nao confere com num_minas")
        self.numeros = [0] * self.total_celulas
        self.minas_posicionadas = True
        self._calcular_numeros()

    def _calcular_numeros(self):
        """Preenche self.numeros: quantas minas há em volta de cada célula.

        Técnica: em vez de perguntar, para cada célula, "quais vizinhas
        são minas?" (L*C*8 consultas ao Conjunto, cada uma O(k)), fazemos
        o contrário: percorremos só as minas e somamos 1 em cada vizinha.
        Conte cada vizinha visitada em "vizinhos_examinados".
        Custo: O(k) — no máximo 8 passos por mina."""
        # TODO 5 (resolvido): para cada mina, somar 1 no numero de cada vizinha
        for mina in self.minas.valores():
            for vizinha in self.vizinhos(mina):
                self.contador.incrementar("vizinhos_examinados")
                self.numeros[vizinha] += 1

    # ------------------------------------------------------------------
    # [Aula 2] Abertura em cascata (flood fill) com Fila ou Pilha
    # ------------------------------------------------------------------

    def _marcar_revelada(self, indice):
        """Abre a célula e atualiza o contador de células seguras. O(1)."""
        self.reveladas[indice] = True
        self.celulas_seguras_restantes -= 1

    def _abrir_a_partir_de(self, inicio):
        """Abre a célula 'inicio'. Se ela for um 0 (nenhuma mina em volta),
        abre também as vizinhas, e as vizinhas das vizinhas que forem 0,
        e assim por diante — a "abertura em cascata".

        Usa uma FILA (abre em ondas: busca em largura) ou uma PILHA (abre
        em profundidade), conforme self.estrategia. As células abertas são
        as mesmas nos dois casos; só a ORDEM muda.

        Regras importantes:
          - Marque a célula como revelada no momento em que ela ENTRA na
            estrutura. Assim ninguém entra duas vezes: cada célula entra
            no máximo uma vez, e a abertura custa O(L*C).
          - Não abra células com bandeira.
          - Vizinhas de um 0 nunca são minas, então não é preciso testar.

        Contadores: "entradas_estrutura" (cada célula colocada),
        "celulas_visitadas" (cada célula retirada), "vizinhos_examinados",
        e registre o maior tamanho da estrutura em "tamanho_max_estrutura".

        Devolve a lista de índices na ordem em que foram retirados da
        estrutura (a interface gráfica usa essa ordem para animar)."""
        # TODO 6 (resolvido): abertura em cascata usando Fila (estrategia "fila") ou Pilha (estrategia "pilha")
        usar_fila = self.estrategia == "fila"
        pendentes = Fila() if usar_fila else Pilha(self.total_celulas)
        colocar = pendentes.enfileirar if usar_fila else pendentes.empilhar
        retirar = pendentes.desenfileirar if usar_fila else pendentes.desempilhar

        ordem = []
        self._marcar_revelada(inicio)          # marca AO COLOCAR na estrutura
        colocar(inicio)
        self.contador.incrementar("entradas_estrutura")
        self.contador.registrar_maximo("tamanho_max_estrutura", pendentes.tamanho())

        while not pendentes.esta_vazia():
            atual = retirar()
            self.contador.incrementar("celulas_visitadas")
            ordem.append(atual)
            if self.numeros[atual] != 0:
                continue                       # célula numerada: abre, mas não espalha
            for vizinha in self.vizinhos(atual):
                self.contador.incrementar("vizinhos_examinados")
                if not self.reveladas[vizinha] and not self.bandeiras.pertence(vizinha):
                    self._marcar_revelada(vizinha)
                    colocar(vizinha)
                    self.contador.incrementar("entradas_estrutura")
                    self.contador.registrar_maximo("tamanho_max_estrutura", pendentes.tamanho())
        return ordem

    # ------------------------------------------------------------------
    # Jogadas. Os métodos públicos (sem "_") são chamados pelas
    # interfaces: eles zeram o contador da jogada, chamam o método
    # interno correspondente e somam a jogada ao total da partida.
    # ------------------------------------------------------------------

    def revelar(self, linha, coluna):
        """Jogada "revelar". Devolve a lista de índices abertos, na ordem
        da abertura (lista vazia se a jogada não fez nada)."""
        self.contador.zerar()
        ordem = self._revelar(self.indice(linha, coluna))
        self.contador_partida.acumular(self.contador)
        return ordem

    def alternar_bandeira(self, linha, coluna):
        """Jogada "bandeira": marca ou desmarca a célula.
        Devolve True se a jogada foi aceita."""
        self.contador.zerar()
        aceita = self._alternar_bandeira(self.indice(linha, coluna))
        self.contador_partida.acumular(self.contador)
        return aceita

    def desfazer(self):
        """Desfaz a última jogada, se ela foi uma bandeira.
        Devolve (linha, coluna) da bandeira desfeita, ou None."""
        self.contador.zerar()
        resultado = self._desfazer()
        self.contador_partida.acumular(self.contador)
        return resultado

    def _revelar(self, indice):
        """Regras da jogada "revelar":
          1. Se a partida acabou, ou a célula já está aberta, ou tem
             bandeira: não faz nada (devolve []).
          2. Se é a primeira jogada: sorteia as minas agora.
          3. Registra a jogada no histórico: ("revelar", linha, coluna).
          4. Se a célula é mina: derrota. Guarda o índice em
             self.mina_explodida e devolve [indice].
          5. Senão, faz a abertura em cascata. Se não restar nenhuma
             célula segura fechada: vitória.
        Custo: O(k) para testar se é mina + O(L*C*f) da abertura, no pior caso."""
        # TODO 7 (resolvido): aplicar as regras da jogada revelar (derrota, abertura e vitoria)
        if self.estado != JOGANDO or self.reveladas[indice] or self.bandeiras.pertence(indice):
            return []
        if not self.minas_posicionadas:
            self._posicionar_minas(indice)

        linha, coluna = self.coordenadas(indice)
        self.historico.empilhar(("revelar", linha, coluna))

        if self.minas.pertence(indice):
            self.estado = DERROTA
            self.mina_explodida = indice
            return [indice]

        ordem = self._abrir_a_partir_de(indice)
        if self.celulas_seguras_restantes == 0:   # vitória verificada em O(1)
            self.estado = VITORIA
        return ordem

    def _alternar_bandeira(self, indice):
        """Marca a célula com bandeira, ou desmarca se já tiver uma.
        Não vale em célula aberta nem com a partida encerrada.
        Registra ("bandeira", linha, coluna) no histórico.
        Custo: O(f) — pertence, inserir e remover no Conjunto."""
        # TODO 8 (resolvido): marcar/desmarcar a bandeira e registrar a jogada no historico
        if self.estado != JOGANDO or self.reveladas[indice]:
            return False
        if self.bandeiras.pertence(indice):
            self.bandeiras.remover(indice)
        else:
            self.bandeiras.inserir(indice)
        linha, coluna = self.coordenadas(indice)
        self.historico.empilhar(("bandeira", linha, coluna))
        return True

    def _desfazer(self):
        """Desfaz a jogada do TOPO da pilha, mas só se ela for uma
        bandeira: revelar não tem volta! Se o topo for um "revelar",
        não faz nada e devolve None. Custo: O(f)."""
        # TODO 9 (resolvido): desfazer a ultima jogada se ela for uma bandeira (consulte o topo da Pilha)
        if self.estado != JOGANDO or self.historico.esta_vazia():
            return None
        acao, linha, coluna = self.historico.consultar_topo()
        if acao != "bandeira":
            return None
        self.historico.desempilhar()
        indice = self.indice(linha, coluna)
        if self.bandeiras.pertence(indice):
            self.bandeiras.remover(indice)
        else:
            self.bandeiras.inserir(indice)
        return linha, coluna

    def ultimas_jogadas(self, quantidade=5):
        """As 'quantidade' jogadas mais recentes, da mais nova para a mais
        antiga, sem alterar o histórico. Custo: O(tamanho do histórico)."""
        # TODO 10 (resolvido): devolver as ultimas jogadas, do topo para a base, sem remover nada
        return self.historico.valores_do_topo_para_base()[:quantidade]

    # ------------------------------------------------------------------
    # Consultas usadas pelas interfaces (já prontas)
    # ------------------------------------------------------------------

    def minas_restantes(self):
        """Minas menos bandeiras — o número do placar. Pode ficar negativo
        se o jogador colocar bandeiras demais. Na vitória, é zero."""
        if self.estado == VITORIA:
            return 0
        return self.num_minas - self.bandeiras.tamanho()

    def mapa_visivel(self):
        """O que o jogador pode ver: uma lista com um código por célula
        (OCULTA, BANDEIRA, MINA, EXPLODIU, ERRO ou o número de 0 a 8).
        No fim da partida, mostra as minas e as bandeiras erradas.
        Custo: O(L*C + k + f), ou O(L*C + k*f) na derrota."""
        mapa = []
        for i in range(self.total_celulas):
            mapa.append(self.numeros[i] if self.reveladas[i] else OCULTA)
        for i in self.bandeiras.valores():
            mapa[i] = BANDEIRA

        if self.estado == DERROTA:
            for i in self.minas.valores():
                if mapa[i] != BANDEIRA:
                    mapa[i] = MINA
            for i in self.bandeiras.valores():
                if not self.minas.pertence(i):
                    mapa[i] = ERRO
            if self.mina_explodida is not None:
                mapa[self.mina_explodida] = EXPLODIU
        elif self.estado == VITORIA:
            for i in self.minas.valores():
                mapa[i] = BANDEIRA               # na vitória, todas as minas viram bandeira
        return mapa


# ======================================================================
# ranking.py
# ======================================================================
# ranking.py
#
# Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
# SOLUÇÃO DE EXEMPLO. Tente primeiro o esqueleto (exercicios/campo_minado/)
# e só depois compare com esta versão.
#
# Ranking dos melhores tempos de cada nível, guardado em um arquivo texto.
#
#   [Aula 1] Cada ranking é uma lista contígua, mantida SEMPRE ordenada
#            pelo tempo (o menor tempo na posição 0).
#   [Aula 4] Inserir um recorde = um passo do Insertion Sort: coloca no fim
#            e desloca para a esquerda até achar o lugar -> O(n).
#            Carregar do arquivo usa o Insertion Sort completo: como o
#            arquivo já é salvo ordenado, cai no MELHOR caso -> Theta(n).
#
# Formato do arquivo (uma linha por recorde):   nivel;tempo_em_segundos;nome
# Exemplo:                                      facil;42.7;Ana
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
    # TODO 11 (resolvido): inserir mantendo a lista ordenada por tempo (um passo do Insertion Sort)
    lista.append(recorde)
    j = len(lista) - 1
    while j > 0 and lista[j - 1][0] > recorde[0]:
        lista[j] = lista[j - 1]          # desloca para a direita
        j -= 1
    lista[j] = recorde
    return j


def ordenar_por_insercao(lista):
    """Ordena a lista de recordes por tempo, no lugar, com Insertion Sort.
    É estável: empates mantêm a ordem original.
    Custo: Theta(n) se a lista já estiver ordenada (o caso do arquivo que
    nós mesmos salvamos); Theta(n^2) no pior caso."""
    # TODO 12 (resolvido): ordenar a lista pelo tempo usando Insertion Sort
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0] > chave[0]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave


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


# ======================================================================
# jogo_terminal.py
# ======================================================================
# jogo_terminal.py
#
# Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
# SOLUÇÃO DE EXEMPLO (este arquivo é igual ao do esqueleto).
#
# Interface de TEXTO do Campo Minado. Funciona em qualquer terminal e
# também em IDEs online, porque só usa print() e input().
#
# Como jogar: digite um comando e tecle Enter.
#     r 3 5   revela a célula da linha 3, coluna 5
#     b 3 5   marca/desmarca uma bandeira na linha 3, coluna 5
#     d       desfaz a última bandeira (a Pilha só deixa desfazer o topo)
#     h       mostra as últimas jogadas (topo da Pilha primeiro)
#     o       mostra as operações contadas na última jogada
#     a       alterna a abertura em cascata entre Fila e Pilha
#     ?       ajuda
#     s       sai da partida
#
# Símbolos:  # fechada   F bandeira   . vazia (0)   1-8 minas em volta
#            * mina   X mina que explodiu   ! bandeira no lugar errado
#
# Este arquivo não tem regras do jogo: ele só lê comandos, chama os
# métodos do Tabuleiro e desenha o resultado.
import time


SIMBOLOS = {OCULTA: "#", BANDEIRA: "F", MINA: "*", EXPLODIU: "X", ERRO: "!", 0: "."}

NOMES_NIVEIS = {"facil": "Facil", "medio": "Medio", "dificil": "Dificil"}

AJUDA = """Comandos (linha e coluna comecam em 1):
  r L C   revela a celula da linha L, coluna C      ex.: r 3 5
  b L C   marca/desmarca bandeira na linha L, coluna C
  d       desfaz a ultima bandeira
  h       mostra as ultimas jogadas (topo da pilha primeiro)
  o       mostra as operacoes contadas na ultima jogada
  a       alterna a abertura em cascata entre Fila e Pilha
  ?       mostra esta ajuda
  s       sai da partida
Simbolos: # fechada  F bandeira  . vazia  1-8 minas em volta
          * mina  X mina que explodiu  ! bandeira errada"""


def simbolo(codigo):
    """Converte o código de mapa_visivel() no caractere exibido."""
    return SIMBOLOS.get(codigo, str(codigo))


def desenhar(tab):
    """Imprime o tabuleiro com os números das linhas e das colunas."""
    mapa = tab.mapa_visivel()
    print()
    print("    " + "".join(f"{c + 1:>3}" for c in range(tab.colunas)))
    for linha in range(tab.linhas):
        # as células da linha ocupam um trecho contíguo da lista [Aula 1]
        trecho = mapa[linha * tab.colunas:(linha + 1) * tab.colunas]
        celulas = "".join(f"{simbolo(codigo):>3}" for codigo in trecho)
        print(f"{linha + 1:>3} {celulas}")
    print(f"Minas restantes: {tab.minas_restantes()}    "
          f"Abertura em cascata: {tab.estrategia.upper()}")


def ler(mensagem):
    """input() que devolve None se a entrada terminar (Ctrl+D / fim do arquivo)."""
    try:
        return input(mensagem)
    except EOFError:
        return None


def interpretar(texto, tab):
    """Converte o texto digitado em (comando, linha, coluna).
    Linha e coluna voltam já convertidas para começar em 0.
    Em caso de erro, devolve ("erro", mensagem, None)."""
    partes = texto.strip().lower().split()
    if not partes:
        return "erro", "Digite um comando (? para ajuda).", None
    comando = partes[0]
    if comando in ("d", "h", "o", "a", "?", "s"):
        return comando, None, None
    if comando in ("r", "b"):
        if len(partes) != 3 or not partes[1].isdigit() or not partes[2].isdigit():
            return "erro", f"Use: {comando} LINHA COLUNA   (ex.: {comando} 3 5)", None
        linha, coluna = int(partes[1]) - 1, int(partes[2]) - 1
        if not (0 <= linha < tab.linhas and 0 <= coluna < tab.colunas):
            return "erro", (f"Posicao fora do tabuleiro: linhas 1 a {tab.linhas}, "
                            f"colunas 1 a {tab.colunas}."), None
        return comando, linha, coluna
    return "erro", "Comando desconhecido (? para ajuda).", None


def escolher_nivel():
    print("\nEscolha o nivel:")
    opcoes = list(NIVEIS)
    for numero, nivel in enumerate(opcoes, start=1):
        linhas, colunas, minas = NIVEIS[nivel]
        print(f"  {numero}) {NOMES_NIVEIS[nivel]:<8} {linhas} x {colunas}, {minas} minas")
    while True:
        resposta = ler("Nivel (1, 2 ou 3): ")
        if resposta is None:
            return None
        if resposta.strip() in ("1", "2", "3"):
            return opcoes[int(resposta) - 1]
        print("Opcao invalida.")


def mostrar_ranking(ranking, nivel):
    recordes = ranking.melhores(nivel)
    print(f"\nRANKING - {NOMES_NIVEIS[nivel]}")
    if not recordes:
        print("  (ainda sem recordes)")
    for posicao, (tempo, nome) in enumerate(recordes, start=1):
        print(f"  {posicao:>2}. {tempo:>7.1f} s   {nome}")


def executar(comando, linha, coluna, tab):
    """Executa um comando de jogo. Devolve False se o jogador quer sair."""
    if comando == "r":
        tab.revelar(linha, coluna)
    elif comando == "b":
        if not tab.alternar_bandeira(linha, coluna):
            print("Nao da para marcar uma celula ja aberta.")
    elif comando == "d":
        desfeita = tab.desfazer()
        if desfeita is None:
            print("Nada a desfazer: so a bandeira do topo da pilha pode ser desfeita")
            print("(revelar nao tem volta).")
        else:
            print(f"Bandeira desfeita na linha {desfeita[0] + 1}, coluna {desfeita[1] + 1}.")
    elif comando == "h":
        jogadas = tab.ultimas_jogadas(5)
        print("Ultimas jogadas (a mais recente primeiro):" if jogadas else "Nenhuma jogada ainda.")
        for acao, l, c in jogadas:
            print(f"  {acao:<9} linha {l + 1}, coluna {c + 1}")
    elif comando == "o":
        print("Operacoes contadas na ultima jogada:")
        print(tab.contador.relatorio())
    elif comando == "a":
        tab.estrategia = "pilha" if tab.estrategia == "fila" else "fila"
        print(f"Abertura em cascata agora usa: {tab.estrategia.upper()}")
    elif comando == "?":
        print(AJUDA)
    elif comando == "s":
        return False
    return True


def jogar_partida(nivel, ranking):
    tab = Tabuleiro(*NIVEIS[nivel])
    print(f"\nNovo jogo: {NOMES_NIVEIS[nivel]}. Digite ? para ver os comandos.")
    inicio = None
    while tab.estado == JOGANDO:
        desenhar(tab)
        texto = ler("> ")
        if texto is None:
            return False                       # a entrada acabou
        comando, linha, coluna = interpretar(texto, tab)
        if comando == "erro":
            print(linha)                       # aqui 'linha' traz a mensagem de erro
            continue
        if comando == "r" and inicio is None:
            inicio = time.monotonic()          # o relógio começa no primeiro clique
        try:
            if not executar(comando, linha, coluna, tab):
                return True
        except NotImplementedError as erro:
            print(f"\nFalta implementar: {erro}")
            print("Complete esse TODO e rode de novo.")
            return False

    desenhar(tab)
    tempo = time.monotonic() - inicio if inicio is not None else 0.0
    if tab.estado == DERROTA:
        print(f"\nBOOM! Voce encontrou uma mina. Tempo: {tempo:.1f} s")
    elif tab.estado == VITORIA:
        print(f"\nPARABENS! Voce abriu todas as celulas seguras em {tempo:.1f} s.")
        if ranking.entraria(nivel, tempo):
            nome = ler("Seu tempo entrou no ranking! Seu nome: ")
            posicao = ranking.registrar(nivel, nome, tempo)
            if not ranking.salvar():
                print("(Nao foi possivel gravar o arquivo do ranking neste ambiente.)")
            print(f"Voce ficou em {posicao}o lugar.")
        mostrar_ranking(ranking, nivel)
    print("\nOperacoes contadas na partida inteira:")
    print(tab.contador_partida.relatorio())
    return True


def main():
    print("=== CAMPO MINADO - Estruturas de Dados, Aula 4 ===")
    ranking = Ranking()
    ranking.carregar()
    while True:
        nivel = escolher_nivel()
        if nivel is None:
            break
        if not jogar_partida(nivel, ranking):
            break
        resposta = ler("\nJogar de novo? (s/n): ")
        if resposta is None or resposta.strip().lower() != "s":
            break
    print("Ate a proxima!")


if __name__ == "__main__":
    main()
