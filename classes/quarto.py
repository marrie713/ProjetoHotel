class Quarto:

    def __init__(self, numero, valor_diaria):
        self.numero = numero
        self.valor_diaria = valor_diaria
        self.ocupado = False

    def ocupar(self):
        self.ocupado = True

    def liberar(self):
        self.ocupado = False

    def exibir_dados(self):
        status = "Ocupado" if self.ocupado else "Livre"

        print(f"Quarto: {self.numero}\n" f"Status: {status}")