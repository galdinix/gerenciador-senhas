from utlis import*
from criptografia import*
class Gerenciador:
    def __init__(self):
        self.contas = {}
        self.chave_verdadeira = 'lucas'

    def armazenarContas(self, conta):
        self.contas[conta.nome_servico] = {'username': conta.username, 'senha': conta.senha}

    def exibirConta(self,nome_servico, chave_seguranca_usuario, gerenciador):
        while True:
            if chave_seguranca_usuario == self.chave_verdadeira:
                if nome_servico in gerenciador.contas:
                    # Se o serviço for encontrado, obter e imprimir a senha descriptografada
                    senha = gerenciador.contas[nome_servico]['senha']
                    senha_descriptografada = descriptografarSenha(senha)
                    print(f"Nome do serviço: {nome_servico}")
                    print(f"Login do serviço: {self.contas[nome_servico]['username']}")
                    print(f"Senha: {senha_descriptografada}")
                    break  # Interromper o loop, pois a senha foi encontrada
                else:
                    # Se o serviço não for encontrado, informar ao usuário e continuar o loop
                    imprimirErro('Serviço não encontrado no gerenciador de senhas!')
                    continue
            else: 
                imprimirErro('Chave de segurança incorreta!')
                



