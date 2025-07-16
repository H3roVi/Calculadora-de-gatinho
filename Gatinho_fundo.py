import customtkinter as ctk
import pygame
from PIL import Image

# Inicializa pygame e mixer
pygame.init()
pygame.mixer.init()

# Carrega som
try:
    miado = pygame.mixer.Sound("miado.wav")
except:
    print("Erro: Arquivo 'miado.wav' não encontrado.")
    miado = None

def tocar_miado():
    if miado:
        miado.play()

# Configura a aparência da janela
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("322x446")
janela.title("Calculadora")

# Carregar imagem de fundo
imagem_fundo = ctk.CTkImage(
    light_image=Image.open("teste.PNG"),
    dark_image=Image.open("teste.PNG"),
    size=(322, 446)
)

# Adiciona a imagem como fundo
label_fundo = ctk.CTkLabel(janela, image=imagem_fundo, text="")
label_fundo.place(x=0, y=0)

# Variáveis globais
todos_valores = ""
valor_texto = ctk.StringVar()

def entrar_valores(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)
    tocar_miado()

def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = ""
    except:
        valor_texto.set("Erro")
        todos_valores = ""
    tocar_miado()

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    tocar_miado()

# Tela de exibição 
display = ctk.CTkEntry(janela, textvariable=valor_texto, width=310, height=90,
                       font=("Ivy", 24), justify="right", fg_color="#50B7F3", text_color="#FFFFFF")
display.place(x=6, y=5)

# Função de criação de botões
def botao(txt, cmd, x, y, w=60, h=60, bg="#FFFFFF", fg="#000000"):
    btn = ctk.CTkButton(janela, text=txt, command=cmd, width=w, height=h,
                        corner_radius=30, fg_color=bg, text_color=fg, font=("Ivy", 18, "bold"))
    btn.place(x=x, y=y)

# Botões
# Linha 1
botao("C", limpar_tela, 6, 100)
botao("%", lambda: entrar_valores('%'), 83, 100)
botao("/", lambda: entrar_valores('/'), 160, 100)
botao("*", lambda: entrar_valores('*'), 237, 100, bg="#F805E4")

# Linha 2
botao("7", lambda: entrar_valores('7'), 6, 170)
botao("8", lambda: entrar_valores('8'), 83, 170)
botao("9", lambda: entrar_valores('9'), 160, 170)
botao("-", lambda: entrar_valores('-'), 237, 170, bg="#F805E4")

# Linha 3
botao("4", lambda: entrar_valores('4'), 6, 240)
botao("5", lambda: entrar_valores('5'), 83, 240)
botao("6", lambda: entrar_valores('6'), 160, 240)
botao("+", lambda: entrar_valores('+'), 237, 240, bg="#F805E4")

# Linha 4
botao("1", lambda: entrar_valores('1'), 6, 310)
botao("2", lambda: entrar_valores('2'), 83, 310)
botao("3", lambda: entrar_valores('3'), 160, 310)
botao("🐾", calcular, 237, 310, h=130, bg="#F805E4")

# Linha 5
botao("0", lambda: entrar_valores('0'), 6, 380, w=137)
botao(".", lambda: entrar_valores('.'), 160, 380)

# Loop principal
janela.mainloop()
