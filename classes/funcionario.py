from classes.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)

    def exibirFuncionario(self):
        pass


