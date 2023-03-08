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