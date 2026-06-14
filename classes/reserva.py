class Reserva:
    def __init__(self):
        self.quartos_disponiveis = [1, 2, 3, 4, 5]
        self.quartos_ocupados = []

    def atribuir_quarto(self):
        print(f"Quartos disponíveis: {self.quartos_disponiveis}")

        quarto = int(input("Escolha um quarto: "))

        if quarto in self.quartos_disponiveis:
            self.quartos_disponiveis.remove(quarto)
            self.quartos_ocupados.append(quarto)

            print(f"Quarto {quarto} reservado com sucesso!")
        else:
            print("Quarto indisponível ou inexistente.")
    
class Reserva:

    def __init__(self, hospede, quarto, dias):
        self.hospede = hospede
        self.quarto = quarto
        self.dias = dias

    def calcular_valor(self):
        return self.quarto.valor_diaria * self.dias

    def gerar_comprovante(self):

        print(f"""
            =========================
            RESERVA
            Hóspede: {self.hospede.nome}
            Quarto: {self.quarto.numero}
            Diárias: {self.dias}
            Valor: R$ {self.calcular_valor()}
            =========================
            """)
