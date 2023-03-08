import tkinter as tk

# Definindo Chave, texto , descriptar e incriptar 
def cifra_cesar(texto, chave, modo):
    resultado = ""
    
    for c in texto:
        if c.isalpha():
            c = c.upper()
            if modo == "encriptar":
                deslocamento = (ord(c) - 65 + chave) % 26
            else:
                deslocamento = (ord(c) - 65 - chave) % 26
            resultado += chr(deslocamento + 65)
        else:
            resultado += c
    
    return resultado

# Criando Funções de encript e descript
def on_click_encriptar():
    mensagem = entrada_mensagem.get()
    chave = int(entrada_chave.get())
    mensagem_encriptada = cifra_cesar(mensagem, chave, "encriptar")
    resultado.config(text=mensagem_encriptada)


def on_click_desencriptar():
    mensagem = entrada_mensagem.get()
    chave = int(entrada_chave.get())
    mensagem_desencriptada = cifra_cesar(mensagem, chave, "descriptar")
    resultado.config(text=mensagem_desencriptada)

# Criar a janela
janela = tk.Tk()
janela.title("Cifra de Cesar Python")

# Loop da janela
janela.mainloop()