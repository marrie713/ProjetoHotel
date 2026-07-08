class Reserva:

    def __init__(self, hospede, quarto, dias):
        self.__hospede = hospede
        self.__quarto = quarto
        self.__dias = dias

    @property
    def hospede(self):
        return self.__hospede

    @property
    def quarto(self):
        return self.__quarto

    @property
    def dias(self):
        return self.__dias

    def calcular_valor(self):
        return self.__dias * self.__quarto.valor_diaria

    def gerar_comprovante(self):

        return (
            "\n================================\n"
            "       RESERVA REALIZADA\n"
            "================================\n"
            f"Hóspede: {self.__hospede.nome}\n"
            f"Quarto: {self.__quarto.numero}\n"
            f"Diárias: {self.__dias}\n"
            f"Valor Total: R$ {self.calcular_valor():.2f}\n"
            "================================"
        )

    def exibir_dados(self):

        return (
            f"Hóspede: {self.__hospede.nome}\n"
            f"Quarto: {self.__quarto.numero}\n"
            f"Diárias: {self.__dias}\n"
            f"Valor Total: R$ {self.calcular_valor():.2f}"
        )
    
    def to_dict(self):
        return {
        "cpf_hospede": self.hospede.cpf,
        "numero_quarto": self.quarto.numero,
        "dias": self.dias
        }