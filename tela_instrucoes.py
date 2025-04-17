import tkinter as tk
from utilitarios import resetaTela
from tela_jogo import TelaJogo

class TelaInstrucoes:
    cor_fundo = "#AFEEEE"

    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game")

    def frameTelaInstrucoes(self):
        # Título
        titulo = tk.Label(
            self.root,
            text="Instruções do Jogo",
            font=("Monaco", 16),
            bg=self.cor_fundo
        )
        titulo.pack(pady=10)

        # Instruções do jogo
        texto = tk.Label(
            self.root,
            text="Clique na operação que corresponde ao resultado entre os dois números mostrados.\nOperações: |+|-|x|÷|",
            font=("Monaco", 15),
            wraplength=600,
            justify="center",
            bg=self.cor_fundo
        )
        texto.pack(pady=10)

        # Botão para iniciar o jogo
        botao_play = tk.Button(
            self.root,
            text="Play",
            font=("Monaco", 16),
            activebackground="#9adbdc",
            command=self.abrirJogo
        )
        botao_play.pack(pady=10)

        # Rodapé com os créditos
        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: Kelly Ramos e Juliana Alves (Senai Betim 2025)",
            font=("Monaco", 10),
            bg=self.cor_fundo
        )
        rodape.pack(side="bottom", pady=10)

    def abrirJogo(self):
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo()
