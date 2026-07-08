class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    # Getters
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    # Setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # Método reutilizado nas classes "filha"
    def exibir_dados(self):
        pass 