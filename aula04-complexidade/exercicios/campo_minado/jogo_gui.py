"""
jogo_gui.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
Este arquivo já vem pronto: você não precisa alterá-lo.

Interface GRÁFICA do Campo Minado, feita com tkinter (que já vem com o
Python no Windows e no macOS; no Linux, instale o pacote python3-tk).

    Clique esquerdo ........ revela a célula
    Clique direito ......... marca/desmarca bandeira (no Mac: Control + clique)
    Ctrl+Z ................. desfaz a última bandeira
    F2 ..................... novo jogo

Menu "Análise":
    - abrir a área vazia com FILA (em ondas) ou com PILHA (em profundidade);
    - animar a abertura, para ver a diferença de ordem entre as duas;
    - numerar as células na ordem em que foram abertas;
    - painel com as operações contadas na última jogada.

Como funciona uma interface gráfica: o programa não tem um laço que lê
comandos, como no terminal. Ele registra FUNÇÕES que o tkinter chama
quando algo acontece (um clique, uma tecla, um tempo que passou) e fica
esperando em raiz.mainloop(). Isso se chama programação orientada a
eventos. As regras do jogo continuam todas em tabuleiro.py.
"""
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

from ranking import Ranking
from tabuleiro import (BANDEIRA, DERROTA, ERRO, EXPLODIU, JOGANDO, MINA,
                       NIVEIS, OCULTA, VITORIA, Tabuleiro)

TAMANHO = 30            # lado de cada célula, em pixels
QUADROS_ANIMACAO = 60   # a animação da abertura dura cerca de 60 quadros
MS_POR_QUADRO = 20      # 60 quadros x 20 ms = 1,2 segundo

# Paleta da disciplina (a mesma dos slides e da apostila)
CORES = {
    "fundo": "#F1F4EF",
    "fechada": "#2E8B79",
    "fechada_brilho": "#5FB3A3",
    "fechada_sombra": "#1C5C4F",
    "aberta": "#F1F4EF",
    "aberta_borda": "#D5DDD3",
    "texto": "#10181C",
    "bandeira": "#E8871E",
    "explodiu": "#E8871E",
    "erro": "#C0392B",
    "ordem": "#8A8F8C",
}
CORES_NUMEROS = {1: "#2B59C3", 2: "#1C7C54", 3: "#C0392B", 4: "#1F2A6B",
                 5: "#7B241C", 6: "#117A65", 7: "#10181C", 8: "#7F8C8D"}
FONTE_NUMERO = ("Helvetica", 14, "bold")
FONTE_ORDEM = ("Helvetica", 7)
FONTE_PAINEL = ("Courier", 10)

NOMES_NIVEIS = {"facil": "Fácil", "medio": "Médio", "dificil": "Difícil"}

COMO_JOGAR = """Objetivo: abrir todas as células que NÃO têm mina.

• Clique esquerdo revela uma célula. Se for uma mina, você perde.
• O número de uma célula aberta diz quantas minas existem nas 8 células em volta dela.
• Uma célula com 0 abre sozinha as vizinhas (abertura em cascata).
• Clique direito (no Mac, Control + clique) marca uma bandeira onde você acha que há uma mina.
• O primeiro clique nunca é uma mina.
• Você vence quando todas as células seguras estiverem abertas."""


class JogoGUI:
    """Janela do jogo. Guarda o Tabuleiro atual e desenha seu estado."""

    def __init__(self, raiz):
        self.raiz = raiz
        raiz.title("Campo Minado — Estruturas de Dados (Aula 4)")
        raiz.configure(bg=CORES["fundo"])
        raiz.resizable(False, False)

        self.ranking = Ranking()
        self.ranking.carregar()

        # Variáveis ligadas aos menus (o tkinter atualiza sozinho)
        self.nivel = tk.StringVar(value="facil")
        self.estrategia = tk.StringVar(value="fila")
        self.animar = tk.BooleanVar(value=True)
        self.numerar_ordem = tk.BooleanVar(value=False)
        self.mostrar_painel = tk.BooleanVar(value=True)

        self.tab = None
        self.inicio = None             # instante do primeiro clique
        self.id_cronometro = None      # identificador do after() do relógio
        self.animando = False
        self.escondidas = []           # células ainda não mostradas na animação
        self.rotulos_ordem = []        # número de ordem de abertura de cada célula

        self._criar_menu()
        self._criar_barra_superior()
        self.canvas = tk.Canvas(raiz, highlightthickness=0, bg=CORES["fundo"])
        self.canvas.grid(row=1, column=0, padx=10, pady=(0, 10))
        self._criar_painel()
        self._ligar_eventos()
        self.novo_jogo()

    # ------------------------------------------------------------------
    # Montagem da janela
    # ------------------------------------------------------------------

    def _criar_menu(self):
        barra = tk.Menu(self.raiz)

        jogo = tk.Menu(barra, tearoff=0)
        jogo.add_command(label="Novo jogo", accelerator="F2", command=self.novo_jogo)
        jogo.add_separator()
        for nivel, (linhas, colunas, minas) in NIVEIS.items():
            jogo.add_radiobutton(label=f"{NOMES_NIVEIS[nivel]} ({linhas}×{colunas}, {minas} minas)",
                                 variable=self.nivel, value=nivel, command=self.novo_jogo)
        jogo.add_separator()
        jogo.add_command(label="Ranking", command=self.mostrar_ranking)
        jogo.add_separator()
        jogo.add_command(label="Sair", command=self.raiz.destroy)
        barra.add_cascade(label="Jogo", menu=jogo)

        analise = tk.Menu(barra, tearoff=0)
        analise.add_radiobutton(label="Abrir com Fila (em ondas)", variable=self.estrategia,
                                value="fila", command=self._trocar_estrategia)
        analise.add_radiobutton(label="Abrir com Pilha (em profundidade)", variable=self.estrategia,
                                value="pilha", command=self._trocar_estrategia)
        analise.add_separator()
        analise.add_checkbutton(label="Animar a abertura", variable=self.animar)
        analise.add_checkbutton(label="Numerar a ordem de abertura", variable=self.numerar_ordem,
                                command=self._desenhar_tudo)
        analise.add_checkbutton(label="Painel de análise", variable=self.mostrar_painel,
                                command=self._alternar_painel)
        barra.add_cascade(label="Análise", menu=analise)

        ajuda = tk.Menu(barra, tearoff=0)
        ajuda.add_command(label="Como jogar", command=lambda: messagebox.showinfo(
            "Como jogar", COMO_JOGAR, parent=self.raiz))
        barra.add_cascade(label="Ajuda", menu=ajuda)

        self.raiz.config(menu=barra)

    def _criar_barra_superior(self):
        barra = tk.Frame(self.raiz, bg=CORES["fundo"])
        barra.grid(row=0, column=0, columnspan=2, sticky="we", padx=10, pady=8)
        self.rotulo_minas = tk.Label(barra, font=("Helvetica", 12, "bold"),
                                     bg=CORES["fundo"], fg=CORES["texto"])
        self.rotulo_minas.pack(side="left")
        self.rotulo_tempo = tk.Label(barra, font=("Helvetica", 12, "bold"),
                                     bg=CORES["fundo"], fg=CORES["texto"])
        self.rotulo_tempo.pack(side="right")
        tk.Button(barra, text="Novo jogo", command=self.novo_jogo).pack(side="left", padx=16)
        self.rotulo_status = tk.Label(barra, font=("Helvetica", 11),
                                      bg=CORES["fundo"], fg=CORES["fechada_sombra"])
        self.rotulo_status.pack(side="left", padx=8)

    def _criar_painel(self):
        self.painel = tk.Label(self.raiz, font=FONTE_PAINEL, justify="left", anchor="nw",
                               bg=CORES["fundo"], fg=CORES["texto"], width=34)
        self.painel.grid(row=1, column=1, sticky="n", padx=(0, 10), pady=(0, 10))

    def _ligar_eventos(self):
        self.canvas.bind("<Button-1>", self._clique_esquerdo)
        # O botão direito tem números diferentes no macOS e nos demais sistemas.
        if self.raiz.tk.call("tk", "windowingsystem") == "aqua":
            self.canvas.bind("<Button-2>", self._clique_direito)
            self.canvas.bind("<Control-Button-1>", self._clique_direito)
        else:
            self.canvas.bind("<Button-3>", self._clique_direito)
        self.raiz.bind("<F2>", lambda evento: self.novo_jogo())
        self.raiz.bind("<Control-z>", lambda evento: self.desfazer())

    # ------------------------------------------------------------------
    # Partida
    # ------------------------------------------------------------------

    def novo_jogo(self):
        self._parar_cronometro()
        self.animando = False
        linhas, colunas, minas = NIVEIS[self.nivel.get()]
        self.tab = Tabuleiro(linhas, colunas, minas)
        self.tab.estrategia = self.estrategia.get()
        self.inicio = None
        self.escondidas = [False] * self.tab.total_celulas
        self.rotulos_ordem = [None] * self.tab.total_celulas
        self.canvas.config(width=colunas * TAMANHO, height=linhas * TAMANHO)
        self.rotulo_tempo.config(text="Tempo: 0")
        self.rotulo_status.config(text="Clique em qualquer célula para começar")
        self._desenhar_tudo()
        self._atualizar_painel()

    def _trocar_estrategia(self):
        if self.tab is not None:
            self.tab.estrategia = self.estrategia.get()
            self._atualizar_painel()

    def _celula_do_evento(self, evento):
        """Converte o pixel clicado em (linha, coluna), ou None se for fora."""
        linha, coluna = evento.y // TAMANHO, evento.x // TAMANHO
        if 0 <= linha < self.tab.linhas and 0 <= coluna < self.tab.colunas:
            return linha, coluna
        return None

    def _indice(self, linha, coluna):
        """Mesma conta do TODO 1, feita aqui para a interface não depender dele."""
        return linha * self.tab.colunas + coluna

    def _pode_jogar(self):
        return not self.animando and self.tab.estado == JOGANDO

    def _clique_esquerdo(self, evento):
        celula = self._celula_do_evento(evento)
        if celula is None or not self._pode_jogar():
            return
        try:
            ordem = self.tab.revelar(*celula)
        except NotImplementedError as erro:
            self._avisar_todo(erro)
            return
        if not ordem:
            return                             # jogada sem efeito
        if self.inicio is None:
            self._iniciar_cronometro()
            self.rotulo_status.config(text="")

        self.rotulos_ordem = [None] * self.tab.total_celulas
        if len(ordem) > 1:
            for posicao, indice in enumerate(ordem, start=1):
                self.rotulos_ordem[indice] = posicao

        self._atualizar_painel()
        if self.animar.get() and len(ordem) > 1:
            self._animar(ordem)
        else:
            self._desenhar_tudo()
            self._verificar_fim()

    def _clique_direito(self, evento):
        celula = self._celula_do_evento(evento)
        if celula is None or not self._pode_jogar():
            return
        try:
            self.tab.alternar_bandeira(*celula)
        except NotImplementedError as erro:
            self._avisar_todo(erro)
            return
        self._desenhar_celula(self._indice(*celula), self.tab.mapa_visivel())
        self._atualizar_placar()
        self._atualizar_painel()

    def desfazer(self):
        if not self._pode_jogar():
            return
        try:
            desfeita = self.tab.desfazer()
        except NotImplementedError as erro:
            self._avisar_todo(erro)
            return
        if desfeita is None:
            self.rotulo_status.config(text="Só bandeiras podem ser desfeitas (topo da pilha)")
            return
        self._desenhar_celula(self._indice(*desfeita), self.tab.mapa_visivel())
        self._atualizar_placar()
        self._atualizar_painel()

    def _verificar_fim(self):
        if self.tab.estado == DERROTA:
            self._parar_cronometro()
            self.rotulo_status.config(text="BOOM! Você encontrou uma mina.")
        elif self.tab.estado == VITORIA:
            self._parar_cronometro()
            tempo = time.monotonic() - self.inicio
            self.rotulo_status.config(text=f"Vitória em {tempo:.1f} s!")
            self._desenhar_tudo()
            self._registrar_recorde(tempo)

    def _registrar_recorde(self, tempo):
        nivel = self.nivel.get()
        if not self.ranking.entraria(nivel, tempo):
            messagebox.showinfo("Vitória!", f"Você venceu em {tempo:.1f} segundos.", parent=self.raiz)
            return
        nome = simpledialog.askstring("Novo recorde!",
                                      f"Você venceu em {tempo:.1f} s e entrou no ranking.\nSeu nome:",
                                      parent=self.raiz)
        self.ranking.registrar(nivel, nome, tempo)
        self.ranking.salvar()
        self.mostrar_ranking()

    # ------------------------------------------------------------------
    # Relógio: after() agenda uma função para daqui a alguns milissegundos
    # ------------------------------------------------------------------

    def _iniciar_cronometro(self):
        self.inicio = time.monotonic()
        self._tique()

    def _tique(self):
        segundos = int(time.monotonic() - self.inicio)
        self.rotulo_tempo.config(text=f"Tempo: {segundos}")
        self.id_cronometro = self.raiz.after(200, self._tique)

    def _parar_cronometro(self):
        if self.id_cronometro is not None:
            self.raiz.after_cancel(self.id_cronometro)
            self.id_cronometro = None

    # ------------------------------------------------------------------
    # Animação da abertura em cascata
    # ------------------------------------------------------------------

    def _animar(self, ordem):
        """Mostra as células abertas aos poucos, na ordem em que saíram da
        Fila ou da Pilha. Com Fila, a área cresce em ondas; com Pilha,
        avança em profundidade, como uma cobra."""
        self.animando = True
        for indice in ordem:
            self.escondidas[indice] = True
        self._desenhar_tudo()
        por_quadro = max(1, len(ordem) // QUADROS_ANIMACAO)
        self._passo_animacao(ordem, 0, por_quadro)

    def _passo_animacao(self, ordem, posicao, por_quadro):
        if not self.animando:
            return                              # um novo jogo interrompeu a animação
        mapa = self.tab.mapa_visivel()
        for indice in ordem[posicao:posicao + por_quadro]:
            self.escondidas[indice] = False
            self._desenhar_celula(indice, mapa)
        posicao += por_quadro
        if posicao < len(ordem):
            self.raiz.after(MS_POR_QUADRO, self._passo_animacao, ordem, posicao, por_quadro)
        else:
            self.animando = False
            self._desenhar_tudo()
            self._verificar_fim()

    # ------------------------------------------------------------------
    # Desenho
    # ------------------------------------------------------------------

    def _desenhar_tudo(self):
        if self.tab is None:
            return
        mapa = self.tab.mapa_visivel()
        self.canvas.delete("all")
        for indice in range(self.tab.total_celulas):
            self._desenhar_celula(indice, mapa)
        self._atualizar_placar()

    def _desenhar_celula(self, indice, mapa):
        """Desenha uma célula. Cada célula tem a etiqueta (tag) "c<indice>",
        para poder ser apagada e redesenhada sozinha."""
        etiqueta = f"c{indice}"
        self.canvas.delete(etiqueta)
        # A interface calcula a posição por conta própria (a mesma conta do
        # TODO 2), para que a janela abra mesmo antes de os TODOs estarem prontos.
        linha, coluna = divmod(indice, self.tab.colunas)
        x0, y0 = coluna * TAMANHO, linha * TAMANHO
        x1, y1 = x0 + TAMANHO, y0 + TAMANHO
        codigo = OCULTA if self.escondidas[indice] else mapa[indice]

        if codigo in (OCULTA, BANDEIRA):
            self._desenhar_fechada(x0, y0, x1, y1, etiqueta)
            if codigo == BANDEIRA:
                self._desenhar_bandeira(x0, y0, etiqueta)
            return

        fundo = CORES["explodiu"] if codigo == EXPLODIU else CORES["aberta"]
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=fundo,
                                     outline=CORES["aberta_borda"], tags=etiqueta)
        if codigo in (MINA, EXPLODIU, ERRO):
            self._desenhar_mina(x0, y0, etiqueta)
            if codigo == ERRO:                  # bandeira errada: mina riscada
                self.canvas.create_line(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=CORES["erro"],
                                        width=3, tags=etiqueta)
                self.canvas.create_line(x0 + 5, y1 - 5, x1 - 5, y0 + 5, fill=CORES["erro"],
                                        width=3, tags=etiqueta)
        elif codigo > 0:
            self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(codigo),
                                    fill=CORES_NUMEROS[codigo], font=FONTE_NUMERO, tags=etiqueta)

        rotulo = self.rotulos_ordem[indice]
        if self.numerar_ordem.get() and rotulo is not None:
            self.canvas.create_text(x0 + 2, y0 + 1, text=str(rotulo), anchor="nw",
                                    fill=CORES["ordem"], font=FONTE_ORDEM, tags=etiqueta)

    def _desenhar_fechada(self, x0, y0, x1, y1, etiqueta):
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=CORES["fechada"],
                                     outline=CORES["fechada_sombra"], tags=etiqueta)
        # um "brilho" em cima e à esquerda dá a impressão de relevo
        self.canvas.create_line(x0 + 1, y1 - 2, x0 + 1, y0 + 1, x1 - 2, y0 + 1,
                                fill=CORES["fechada_brilho"], width=2, tags=etiqueta)

    def _desenhar_bandeira(self, x0, y0, etiqueta):
        self.canvas.create_line(x0 + 11, y0 + 7, x0 + 11, y0 + 24, fill=CORES["texto"],
                                width=2, tags=etiqueta)
        self.canvas.create_polygon(x0 + 12, y0 + 7, x0 + 23, y0 + 11, x0 + 12, y0 + 15,
                                   fill=CORES["bandeira"], outline=CORES["texto"], tags=etiqueta)
        self.canvas.create_line(x0 + 7, y0 + 24, x0 + 17, y0 + 24, fill=CORES["texto"],
                                width=2, tags=etiqueta)

    def _desenhar_mina(self, x0, y0, etiqueta):
        cx, cy = x0 + TAMANHO // 2, y0 + TAMANHO // 2
        for dx, dy in ((9, 0), (0, 9), (6, 6), (6, -6)):   # espinhos
            self.canvas.create_line(cx - dx, cy - dy, cx + dx, cy + dy, fill=CORES["texto"],
                                    width=2, tags=etiqueta)
        self.canvas.create_oval(cx - 6, cy - 6, cx + 6, cy + 6, fill=CORES["texto"],
                                outline=CORES["texto"], tags=etiqueta)
        self.canvas.create_oval(cx - 3, cy - 3, cx - 1, cy - 1, fill="#FFFFFF",
                                outline="#FFFFFF", tags=etiqueta)

    def _atualizar_placar(self):
        self.rotulo_minas.config(text=f"Minas: {self.tab.minas_restantes()}")

    # ------------------------------------------------------------------
    # Painel de análise [Aula 4]
    # ------------------------------------------------------------------

    def _alternar_painel(self):
        if self.mostrar_painel.get():
            self.painel.grid()
        else:
            self.painel.grid_remove()

    def _atualizar_painel(self):
        nome = "FILA (em ondas)" if self.tab.estrategia == "fila" else "PILHA (em profundidade)"
        linhas = [f"Abertura: {nome}", "", "Última jogada:"]
        linhas += ["  " + linha for linha in self.tab.contador.relatorio().splitlines()]
        linhas += ["", "Partida inteira:"]
        linhas += ["  " + linha for linha in self.tab.contador_partida.relatorio().splitlines()]
        linhas += ["", "Histórico (topo primeiro):"]
        try:
            jogadas = self.tab.ultimas_jogadas(5)
        except NotImplementedError:
            jogadas = []
            linhas.append("  (falta o TODO 10)")
        for acao, linha, coluna in jogadas:
            linhas.append(f"  {acao:<9} ({linha + 1}, {coluna + 1})")
        self.painel.config(text="\n".join(linhas))

    # ------------------------------------------------------------------
    # Janelas auxiliares
    # ------------------------------------------------------------------

    def mostrar_ranking(self):
        janela = tk.Toplevel(self.raiz)
        janela.title("Ranking")
        janela.configure(bg=CORES["fundo"])
        partes = []
        for nivel in NIVEIS:
            partes.append(f"{NOMES_NIVEIS[nivel].upper()}")
            recordes = self.ranking.melhores(nivel)
            if not recordes:
                partes.append("   (ainda sem recordes)")
            for posicao, (tempo, nome) in enumerate(recordes, start=1):
                partes.append(f"  {posicao:>2}. {tempo:>7.1f} s  {nome}")
            partes.append("")
        tk.Label(janela, text="\n".join(partes), font=FONTE_PAINEL, justify="left",
                 bg=CORES["fundo"], fg=CORES["texto"]).pack(padx=16, pady=12)
        tk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=(0, 12))

    def _avisar_todo(self, erro):
        messagebox.showwarning("Falta implementar",
                               f"{erro}\n\nComplete esse TODO e rode o jogo de novo.",
                               parent=self.raiz)


def main():
    raiz = tk.Tk()
    JogoGUI(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
