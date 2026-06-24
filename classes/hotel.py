from classes.hospede import Hospede
from classes.funcionario import Funcionario
from classes.quarto import Quarto
from classes.reserva import Reserva

class Hotel:
    def __init__(self):
        self.hospedes = []
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def cadastrar_hospede(self, nome, telefone):
        hospede = Hospede(nome, telefone)
        self.hospedes.append(hospede)
        print("Hospede cadastrado com sucesso!")
        print(f"nome: {nome} telefone: {telefone}")
    
    def cadastrar_funcionario(self, nome, telefone, cargo):
        funcionarioo = Funcionario(nome, telefone, cargo)
        self.funcionarios.append(funcionarioo)
        print("Funcionario cadastrado com sucesso!")
        print(f"nome: {nome} telefone: {telefone} cargo: {cargo}")

    def cadastrar_quarto(self, numero, tipo, valor):

        quarto = Quarto(numero, tipo, valor)

        self.quartos.append(quarto)

    def realizar_reserva(self, cpf, numero_quarto, dias):

        hospede = None
        quarto = None

        for h in self.hospedes:
            if h.cpf == cpf:
                hospede = h

        for q in self.quartos:
            if q.numero == numero_quarto:
                quarto = q

        if hospede and quarto and not quarto.ocupado:

            reserva = Reserva(hospede, quarto, dias)

            self.reservas.append(reserva)

            quarto.ocupar()

            print(reserva.gerar_comprovante())

    def listar_quartos_disponiveis(self):

        for quarto in self.quartos:

            if not quarto.ocupado:
                print(quarto.exibir_dados())

    def listar_quartos_ocupados(self):

        for quarto in self.quartos:

            if quarto.ocupado:
                print(quarto.exibir_dados())

    def gerar_relatorio(self):

        print(f"Total de hóspedes: {len(self.hospedes)}")
        print(f"Total de quartos: {len(self.quartos)}")
        print(f"Total de reservas: {len(self.reservas)}")