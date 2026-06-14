from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, cep):
        super().__init__(nome, telefone, cep)

    def exibirFuncionario(self):
        print("")


