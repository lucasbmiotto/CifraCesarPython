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

# ||||||||||   CRIAÇÃO DA PARTE GRÁFICA   ||||||||||

# Criar a janela
janela = tk.Tk()
janela.title("Cifra de Cesar Python")

# Criar o título
titulo = tk.Label(janela, text="Cifra de Cesar Python", font=("Helvetica", 16, "bold"), pady=20)
titulo.pack()

# Criar a entrada para a chave
label_chave = tk.Label(janela, text="Chave:")
label_chave.pack()
entrada_chave = tk.Entry(janela)
entrada_chave.pack()

# Criar os botões para encriptar e desencriptar
botao_encriptar = tk.Button(janela, text="Encriptar", command=on_click_encriptar)
botao_encriptar.pack(side=tk.LEFT, padx=20, pady=20)
botao_desencriptar = tk.Button(janela, text="Desencriptar", command=on_click_desencriptar)
botao_desencriptar.pack(side=tk.LEFT, padx=20, pady=20)

# Criar a entrada para a mensagem
label_mensagem = tk.Label(janela, text="Mensagem:")
label_mensagem.pack()
entrada_mensagem = tk.Entry(janela)
entrada_mensagem.pack()

# Criar o resultado
resultado = tk.Label(janela, text="", font=("Helvetica", 14), pady=20)
resultado.pack()

# Loop da janela
janela.mainloop()