import tkinter as tk
from tela_instrucoes import TelaInstrucoes
from utilitarios import resetaTela

class TelaInicial:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game")
        self.root.configure(bg="#AFEEEE")  # Define a cor de fundo da janela

    def frameTelaInicial(self): 
        titulo = tk.Label(
            self.root,
            text="The Math Game",
            font=("Monaco", 34),
            bg="#AFEEEE"  # Cor de fundo do texto
        )
        titulo.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Play",
            font=("Monaco", 16),
            command=self.abrirInstrucoes,
            activebackground="#AFEEEE"  # Para manter a cor quando clicar
        )
        botao_play.pack(pady=10)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: Kelly Ramos e Juliana Alves (Senai Betim 2025)",
            font=("Monaco", 10),
            bg="#AFEEEE"  # Cor de fundo do rodapé
        )
        rodape.pack(side="bottom", pady=10)

    def abrirInstrucoes(self):
        tela_inicial = TelaInstrucoes(self.root)    
        tela_inicial.frameTelaInstrucoes()
