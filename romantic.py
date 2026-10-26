import tkinter as tk
from tkinter import font


def coracao_poliglota():
    mensagens = [
        "  Te amo!  ",
        " I love you",
        " Je t'aime ",
        " Ti amo... ",
        "Ich liebe d",
        "  Saranghae",
        "Aishiteru  ",
        " Ya tebya l",
        " Wo ai ni  ",
        "  Seviyorum",
        "  Te quiero",
        " Mahal kita",
        "    Rohayhu",
    ]

    matriz_coracao = [
        [0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]

    janela = tk.Tk()
    janela.configure(bg="black")
    janela.attributes("-fullscreen", True)
    janela.bind("<Escape>", lambda _evento: janela.destroy())

    tela = tk.Canvas(janela, bg="black", highlightthickness=0)
    tela.pack(fill="both", expand=True)
    janela.update_idletasks()

    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    tamanho_fonte = max(8, min(largura // 52, altura // 18))
    fonte = font.Font(family="Consolas", size=tamanho_fonte, weight="bold")
    largura_bloco = fonte.measure("0" * 11)
    altura_linha = fonte.metrics("linespace")
    inicio_x = (largura - largura_bloco * 7) / 2
    inicio_y = (altura - altura_linha * len(matriz_coracao)) / 2

    indice_mensagem = 0

    def mostrar_linha(indice_linha):
        nonlocal indice_mensagem
        if indice_linha == len(matriz_coracao):
            return

        y = inicio_y + indice_linha * altura_linha
        for coluna, preenchido in enumerate(matriz_coracao[indice_linha]):
            if preenchido:
                x = inicio_x + coluna * largura_bloco
                tela.create_text(
                    x,
                    y,
                    text=mensagens[indice_mensagem % len(mensagens)],
                    anchor="nw",
                    font=fonte,
                    fill="#ff1744",
                )
                indice_mensagem += 1

        janela.after(250, mostrar_linha, indice_linha + 1)

    mostrar_linha(0)
    janela.mainloop()


# Executa o código
coracao_poliglota()
