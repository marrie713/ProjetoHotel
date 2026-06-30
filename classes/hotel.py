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

        #os 10 quartos do hotel
        for numero in range(1, 11):
            self.quartos.append(Quarto(numero))

    #hóspede
    def cadastrar_hospede(self, nome, cpf, telefone):

        for hospede in self.hospedes:
            if hospede.cpf == cpf:
                print("Já existe um hóspede com esse CPF.")
                return

        hospede = Hospede(nome, cpf, telefone)
        self.hospedes.append(hospede)

        print("Hóspede cadastrado com sucesso!")

    def listar_hospedes(self):

        if not self.hospedes:
            print("Nenhum hóspede cadastrado.")
            return

        for hospede in self.hospedes:
            print(hospede.exibir_dados())
            print("-" * 30)


    #funcionário
    def cadastrar_funcionario(self, nome, cpf, telefone, cargo):

        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                print("Já existe um funcionário com esse CPF.")
                return

        funcionario = Funcionario(nome, cpf, telefone, cargo)

        self.funcionarios.append(funcionario)

        print("Funcionário cadastrado com sucesso!")

    def listar_funcionarios(self):

        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        for funcionario in self.funcionarios:
            print(funcionario.exibir_dados())
            print("-" * 30)

    #quartos
    def listar_quartos_disponiveis(self):

        encontrou = False

        for quarto in self.quartos:

            if not quarto.ocupado:
                print(quarto.exibir_dados())
                print("-" * 30)
                encontrou = True

        if not encontrou:
            print("Não há quartos disponíveis.")

    def listar_quartos_ocupados(self):

        encontrou = False

        for quarto in self.quartos:

            if quarto.ocupado:
                print(quarto.exibir_dados())
                print("-" * 30)
                encontrou = True

        if not encontrou:
            print("Não há quartos ocupados.")

    #reservas
    def realizar_reserva(self, cpf, numero_quarto, dias):

        hospede = None
        quarto = None

        # Procura o hóspede
        for h in self.hospedes:
            if h.cpf == cpf:
                hospede = h
                break

        if hospede is None:
            print("Hóspede não encontrado.")
            return

        # Procura o quarto
        for q in self.quartos:
            if q.numero == numero_quarto:
                quarto = q
                break

        if quarto is None:
            print("Quarto não encontrado.")
            return

        if quarto.ocupado:
            print("Esse quarto já está ocupado.")
            return

        reserva = Reserva(hospede, quarto, dias)

        self.reservas.append(reserva)

        quarto.ocupar()

        print(reserva.gerar_comprovante())

    def listar_reservas(self):

        if not self.reservas:
            print("Nenhuma reserva cadastrada.")
            return

        for reserva in self.reservas:
            print(reserva.exibir_dados())
            print("-" * 30)

    #check-out

    def finalizar_reserva(self, numero_quarto):

        for reserva in self.reservas:

            if reserva.quarto.numero == numero_quarto:

                reserva.quarto.liberar()

                self.reservas.remove(reserva)

                print("Reserva finalizada com sucesso!")
                return

        print("Reserva não encontrada.")

    #relatório

    def gerar_relatorio(self):

        print("\n===== RELATÓRIO =====")

        print(f"Hóspedes cadastrados: {len(self.hospedes)}")
        print(f"Funcionários cadastrados: {len(self.funcionarios)}")
        print(f"Quartos: {len(self.quartos)}")
        print(f"Reservas ativas: {len(self.reservas)}")

        livres = 0
        ocupados = 0

        for quarto in self.quartos:

            if quarto.ocupado:
                ocupados += 1
            else:
                livres += 1

        print(f"Quartos disponíveis: {livres}")
        print(f"Quartos ocupados: {ocupados}")