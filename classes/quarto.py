class Quarto:

    VALOR_DIARIA = 150

    def __init__(self, numero):
        self.__numero = numero
        self.__ocupado = False

    @property
    def numero(self):
        return self.__numero

    @property
    def valor_diaria(self):
        return Quarto.VALOR_DIARIA

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, ocupado):
        self.__ocupado = ocupado

    def ocupar(self):
        self.__ocupado = True

    def liberar(self):
        self.__ocupado = False

    def exibir_dados(self):

        status = "Ocupado" if self.__ocupado else "Disponível"

        return (
            f"Quarto: {self.__numero}\n"
            f"Valor da diária: R$ {self.valor_diaria:.2f}\n"
            f"Status: {status}"
        )
    
    def to_dict(self):
        return {
        "numero": self.numero,
        "ocupado": self.ocupado
        }