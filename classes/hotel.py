from hospede import Hospede

class Hotel:
    def __init__(self):
        self.hospedes = []

    def cadastrar_hospede(self, nome, telefone):
        hospede = Hospede(nome, telefone)
        self.hospedes.append(hospede)
        print("Hospede cadastrado com sucesso!")
    
    def cadastrar_funcionario(self, cargo):
        cargo = input("Informe o cargo do funcionario:")
        print("funcionario cadastrado com sucesso!")
        print(f"Funcionario:{self.nome} cargo: {cargo}")