from classes.hospede import Hospede
from classes.funcionario import Funcionario
from classes.quarto import Quarto
from classes.reserva import Reserva
from utils.persistencia import Persistencia

class Hotel:

    def __init__(self):
        self.hospedes = []
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

        # 1. Carregar Hóspedes
        dados_hospedes = Persistencia.carregar("hospedes.json")
        for d in dados_hospedes:
            self.hospedes.append(Hospede(d["nome"], d["cpf"], d["telefone"]))

        # 2. Carregar Funcionários
        dados_funcionarios = Persistencia.carregar("funcionarios.json")
        for d in dados_funcionarios:
            self.funcionarios.append(Funcionario(d["nome"], d["cpf"], d["telefone"], d["cargo"]))

        # 3. Carregar Quartos (Se não houver JSON, cria os 10 quartos padrão)
        dados_quartos = Persistencia.carregar("quartos.json")
        if not dados_quartos:
            for numero in range(1, 11):
                self.quartos.append(Quarto(numero))
        else:
            for d in dados_quartos:
                quarto = Quarto(d["numero"])
                quarto.ocupado = d["ocupado"]
                self.quartos.append(quarto)

        # 4. Carregar Reservas
        dados_reservas = Persistencia.carregar("reservas.json")
        for d in dados_reservas:
            hospede_encontrado = next((h for h in self.hospedes if h.cpf == d["cpf_hospede"]), None)
            quarto_encontrado = next((q for q in self.quartos if q.numero == d["numero_quarto"]), None)
            
            if hospede_encontrado and quarto_encontrado:
                self.reservas.append(Reserva(hospede_encontrado, quarto_encontrado, d["dias"]))

    # Método para persistir as alterações de estado
    def _salvar_dados(self):
        Persistencia.salvar("hospedes.json", [h.to_dict() for h in self.hospedes])
        Persistencia.salvar("funcionarios.json", [f.to_dict() for f in self.funcionarios])
        Persistencia.salvar("quartos.json", [q.to_dict() for q in self.quartos])
        Persistencia.salvar("reservas.json", [r.to_dict() for r in self.reservas])

    def cadastrar_hospede(self, nome, cpf, telefone):
        for hospede in self.hospedes:
            if hospede.cpf == cpf:
                return False

        hospede = Hospede(nome, cpf, telefone)
        self.hospedes.append(hospede)
        self._salvar_dados() # Salva no JSON após alterar a lista

        return True
    
    def listar_hospedes(self):
        if not self.hospedes:
            print("Nenhum hóspede cadastrado.")
            return
        for hospede in self.hospedes:
            print(hospede.exibir_dados())
            print("-" * 30)

    def cadastrar_funcionario(self, nome, cpf, telefone, cargo):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return False

        funcionario = Funcionario(nome, cpf, telefone, cargo)
        self.funcionarios.append(funcionario)
        self._salvar_dados()
        
        return True

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        for funcionario in self.funcionarios:
            print(funcionario.exibir_dados())
            print("-" * 30)

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

    def realizar_reserva(self, cpf, numero_quarto, dias):
        hospede = None
        quarto = None

        for h in self.hospedes:
            if h.cpf == cpf:
                hospede = h
                break

        if hospede is None:
            print("Hóspede não encontrado.")
            return False

        for q in self.quartos:
            if q.numero == numero_quarto:
                quarto = q
                break

        if quarto is None:
            print("Quarto não encontrado.")
            return False

        if quarto.ocupado:
            print("Esse quarto já está ocupado.")
            return False

        reserva = Reserva(hospede, quarto, dias)
        self.reservas.append(reserva)
        quarto.ocupar()
        
        self._salvar_dados() # Salva as novas reservas e o estado do quarto no JSON
        return True

    def listar_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva cadastrada.")
            return
        for reserva in self.reservas:
            print(reserva.exibir_dados())
            print("-" * 30)

    def finalizar_reserva(self, numero_quarto):
        for reserva in self.reservas:
            if reserva.quarto.numero == numero_quarto:
                reserva.quarto.liberar()
                self.reservas.remove(reserva)
                
                self._salvar_dados() # Salva a remoção da reserva e a liberação do quarto
                
                print("Reserva finalizada com sucesso!")
                return
        print("Reserva não encontrada.")

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