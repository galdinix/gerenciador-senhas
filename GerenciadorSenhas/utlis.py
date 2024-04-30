from validations import*
import time

def receberUsername():
    while True:
        try:
            username = input('Informe o nome de usuário(login): ').lower().strip()
            return username
        except KeyboardInterrupt:
            imprimirErro('Erro, insinra um nome')

def receberTamanhoSenha():
    while True:
        try:
            tamanho_senha = int(input('Informe o tamanho da senha desejada: '))
            if isTamanhoSenhaValid(tamanho_senha):
                return tamanho_senha
            imprimirErro('Informe um inteiro positivo maior que 4')
        except ValueError:
            imprimirErro('Informe um número inteiro')


def receberNomeServico():
    while True:
        try:
            nome_servico = input('Informe o nome do serviço: ')
            return nome_servico
        except KeyboardInterrupt:
            imprimirErro('Erro, insinra um nome')

def receberChaveSeguranca():
    while True:
        try:
            nome_servico = input('Informe a chave de segurança: ').lower().strip()
            return nome_servico
        except KeyboardInterrupt:
            imprimirErro('Erro, insinra um nome')

def imprimirErro(acao, tempo = 0.4):
    for i in range(5):  # Define a quantidade de pontos
        print(acao, '.' * i, end='\r')  # Imprime os pontos
        time.sleep(tempo)

def exibirMenu():
    print('\n\nDigite 1 para gerar contas: ')
    print('Digite 2 para consultar contas: ')

def receberRespostaMenu():
    while True:
        try:
            opc = int(input('Informe a opção do menu: '))
            if isOpcValid(opc):
                return opc
            imprimirErro('Informe um número válido')
        except ValueError:
            imprimirErro('Erro, informe um número')