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
janela.geometry("600x500")
janela.title("Cifra de Cesar Python")
janela.configure(bg="#F5F5F5")

# Criar o título
titulo = tk.Label(janela, text="Cifra de Cesar Python", font=("Helvetica", 24, "bold"), pady=20, bg="#F5F5F5")
titulo.pack()

# Criar o frame para a entrada da chave
frame_chave = tk.Frame(janela, bg="#F5F5F5")
frame_chave.pack(pady=10)
label_chave = tk.Label(frame_chave, text="Chave:", font=("Helvetica", 16), bg="#F5F5F5")
label_chave.pack(side=tk.LEFT)
entrada_chave = tk.Entry(frame_chave, font=("Helvetica", 16), width=5)
entrada_chave.pack(side=tk.LEFT, padx=10)

# Criar os botões para encriptar e desencriptar
frame_botoes = tk.Frame(janela, bg="#F5F5F5")
frame_botoes.pack(pady=20)
botao_encriptar = tk.Button(frame_botoes, text="Encriptar", font=("Helvetica", 16), command=on_click_encriptar)
botao_encriptar.pack(side=tk.LEFT, padx=20)
botao_desencriptar = tk.Button(frame_botoes, text="Desencriptar", font=("Helvetica", 16), command=on_click_desencriptar)
botao_desencriptar.pack(side=tk.LEFT, padx=20)

# Criar a entrada para a mensagem
label_mensagem = tk.Label(janela, text="Mensagem:", font=("Helvetica", 16), bg="#F5F5F5")
label_mensagem.pack()
entrada_mensagem = tk.Entry(janela, font=("Helvetica", 16))
entrada_mensagem.pack(pady=10)


# Criar o frame para o resultado
frame_resultado = tk.Frame(janela, bg="#F5F5F5")
frame_resultado.pack(pady=20)
label_resultado = tk.Label(frame_resultado, text="Resultado:", font=("Helvetica", 16), bg="#F5F5F5")
label_resultado.pack(side=tk.LEFT)
resultado = tk.Label(frame_resultado, text="", font=("Helvetica", 16), bg="#F5F5F5")
resultado.pack(side=tk.LEFT, padx=10)

# Iniciar a janela
janela.mainloop()