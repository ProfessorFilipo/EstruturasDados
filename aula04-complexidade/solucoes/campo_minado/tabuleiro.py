"""
tabuleiro.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
SOLUÇÃO DE EXEMPLO. Tente primeiro o esqueleto (exercicios/campo_minado/)
e só depois compare com esta versão.

Toda a LÓGICA do jogo, sem nenhuma interface: nada de print, nada de
janela. As interfaces (jogo_terminal.py e jogo_gui.py) apenas chamam os
métodos públicos desta classe e desenham o resultado. Assim, a mesma
lógica serve para as duas — e pode ser testada sozinha (testes.py).

Onde cada aula aparece:

  [Aula 1] O tabuleiro é guardado em LISTAS LINEARES (contíguas): a célula
           (linha, coluna) fica na posição  linha * colunas + coluna,
           então ler ou alterar qualquer célula custa O(1).
  [Aula 2] FILA para abrir a área vazia em "ondas" (busca em largura);
           PILHA para abrir em profundidade e para o histórico de jogadas.
  [Aula 3] CONJUNTO para sortear as minas sem repetição e para as bandeiras.
  [Aula 4] Cada método informa seu custo, e o contador de operações mede
           o trabalho de cada jogada.

Convenções:
  - No código, linhas e colunas começam em 0. As interfaces mostram a
    partir de 1 para o jogador.
  - L = linhas, C = colunas, k = número de minas, f = número de bandeiras.
"""
import random

from estruturas import Conjunto, ContadorOperacoes, Fila, Pilha

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
