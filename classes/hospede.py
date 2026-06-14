from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, nome, telefone, cep):
        super().__init__(nome, telefone, cep)

    def exibir_hospede(self):
        print(f"-----CADASTRO DO HÓSPEDE-----\nNome: {self.nome}\nTelefone: {self.telefone}\nCep: {self.cep}")

