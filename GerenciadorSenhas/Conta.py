class Conta():
    def __init__(self, username, senha, nome_servico  ):
        self.username = username
        self.senha = senha
        self.nome_servico = nome_servico
      
    def __str__(self) -> str:
        return str(f'{self.username}')
        