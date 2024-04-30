def isTamanhoSenhaValid(tamanho_senha):
    if tamanho_senha < 4:
        return False
    return True

def isOpcValid(opc):
    if opc >= 0 and opc <= 2:
        return True
    return False