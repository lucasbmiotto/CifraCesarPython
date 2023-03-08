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
janela.geometry("500x400")
janela.title("Cifra de Cesar Python")

# Criar o título
titulo = tk.Label(janela, text="Cifra de Cesar Python", font=("Helvetica", 20, "bold"), pady=20)
titulo.pack()

# Criar o frame para a entrada da chave
frame_chave = tk.Frame(janela)
frame_chave.pack(pady=10)
label_chave = tk.Label(frame_chave, text="Chave:", font=("Helvetica", 14))
label_chave.pack(side=tk.LEFT)
entrada_chave = tk.Entry(frame_chave, font=("Helvetica", 14), width=5)
entrada_chave.pack(side=tk.LEFT, padx=10)

# Criar os botões para encriptar e desencriptar
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)
botao_encriptar = tk.Button(frame_botoes, text="Encriptar", font=("Helvetica", 14), command=on_click_encriptar)
botao_encriptar.pack(side=tk.LEFT, padx=20)
botao_desencriptar = tk.Button(frame_botoes, text="Desencriptar", font=("Helvetica", 14), command=on_click_desencriptar)
botao_desencriptar.pack(side=tk.LEFT, padx=20)

# Criar a entrada para a mensagem
label_mensagem = tk.Label(janela, text="Mensagem:", font=("Helvetica", 14))
label_mensagem.pack()
entrada_mensagem = tk.Entry(janela, font=("Helvetica", 14), width=40)
entrada_mensagem.pack()

# Criar o resultado
resultado = tk.Label(janela, text="", font=("Helvetica", 16), pady=20)
resultado.pack()

# Loop da janela
janela.mainloop()