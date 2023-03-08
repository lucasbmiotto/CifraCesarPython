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

# Teste de Cifra
texto_original = "Hello"
chave = 3
texto_encriptado = cifra_cesar(texto_original, chave, "encriptar")
print("Texto encriptado:", texto_encriptado)
texto_desencriptado = cifra_cesar(texto_encriptado, chave, "descriptar")
print("Texto desencriptado:", texto_desencriptado)