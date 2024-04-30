import random
import string
import criptografia 

def gerarSenha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    caracteres_escolhidos = [random.choice(caracteres) for i in range(tamanho)]
    senha = ''.join(caracteres_escolhidos)
    senha_criptografada = criptografia.criptografarSenha(senha)
    return senha_criptografada




