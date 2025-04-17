import tkinter as tk
from tkinter import messagebox
from tela_abertura import TelaInicial

def frameGenerico():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("🧠The Math Game🧠")
    root.resizable(False, False) 
    root.config(bg="#AFEEEE")
    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True
    
    def funcao_fechar():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            root.running = False
            root.continua_jogo.set(True)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", funcao_fechar)

    # Texto centralizado
    texto_label = tk.Label(root, text="Bem-vindo ao The Math Game!", font=("Arial", 24), bg="#AFEEEE", fg="black")
    texto_label.place(relx=0.5, rely=0.4, anchor="center")  # Centralizando o texto


    return root
root = frameGenerico()
tela_inicial = TelaInicial(root)
tela_inicial.frameTelaInicial()

try:
    root.mainloop()
except Exception as e:
    print(f"Erro durante a execução: {e}")
