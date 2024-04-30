num_especiais_letras = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'á', 'à', 'ã', 'â', 'b', 'c', 'ç', 'd', 'e', 'é', 'ê', 'f', 'g', 'h', 'i', 'í', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'õ', 'ô', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'v', 'w', 'x', 'y', 'z']

def criptografarSenha(texto):
    texto_modificado = []
    for caractere in texto:
        if caractere in num_especiais_letras:
            indice_original = num_especiais_letras.index(caractere)
            indice_novo = (indice_original + 5) % len(num_especiais_letras)
            texto_modificado.append(num_especiais_letras[indice_novo])
        else:
            texto_modificado.append(caractere)
    return ''.join(texto_modificado)

def descriptografarSenha(texto): 
    texto_modificado = []
    for caractere in texto:
        if caractere in num_especiais_letras:
            indice_original = num_especiais_letras.index(caractere)
            indice_novo = (indice_original - 5) % len(num_especiais_letras)
            texto_modificado.append(num_especiais_letras[indice_novo])
        else:
            texto_modificado.append(caractere)
    return ''.join(texto_modificado)




    