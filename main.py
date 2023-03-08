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

# Pedir entrada do usuário
mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave (um número inteiro positivo): "))
modo = input("Deseja encriptar ou descriptar? ").lower()

# Validar entrada do usuário
if modo not in ["encriptar", "descriptar"]:
    print("Modo inválido. Use 'encriptar' ou 'descriptar'.")
    exit()

# Chamar a função de acordo com a escolha do usuário
if modo == "encriptar":
    mensagem_encriptada = cifra_cesar(mensagem, chave, "encriptar")
    print("Mensagem encriptada:", mensagem_encriptada)
else:
    mensagem_desencriptada = cifra_cesar(mensagem, chave, "descriptar")
    print("Mensagem desencriptada:", mensagem_desencriptada)