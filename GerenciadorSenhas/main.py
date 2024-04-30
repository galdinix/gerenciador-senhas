from Conta import Conta
from Gerenciador import Gerenciador
from utlis import*
from criptografia import*
from Gerador import*
gerenciador = Gerenciador()

def criarSenha():
    username = receberUsername()
    tamanho_senha = receberTamanhoSenha()
    senha_criptografada = gerarSenha(tamanho_senha)
    nome_servico = receberNomeServico()
    conta = Conta(username, senha_criptografada, nome_servico)
    gerenciador.armazenarContas(conta)

def consultarConta():
    nome_servico = receberNomeServico()
    chave_seguranca_usuario = receberChaveSeguranca()
    gerenciador.exibirConta(nome_servico, chave_seguranca_usuario, gerenciador)
    

def main():
    while True: 
        exibirMenu()
        opc = receberRespostaMenu()
        if opc == 1: 
            print('\n\t\tBem vindo a criação de senhas\n')
            criarSenha()
            continue
        if opc == 2:
            print('\n\t\tBem vindo a consulta de senhas\n')
            consultarConta()
            continue
        print('Encerrando....')


main()

