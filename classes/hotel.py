class Hotel:
    def __init__(self):
        self.hospedes = []

    def cadastrar_hospede(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")

        hospede = Hospede(nome, cpf)
        self.hospedes.append(hospede)

        print("Hóspede cadastrado com sucesso!")