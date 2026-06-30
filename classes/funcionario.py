from classes.pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, telefone, cargo):
        super().__init__(nome, cpf, telefone)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    def exibir_dados(self):
        return (
            f"Funcionário\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self.telefone}\n"
            f"Cargo: {self.cargo}"
        )
    
    def to_dict(self):
        return {
        "nome": self.nome,
        "cpf": self.cpf,
        "telefone": self.telefone,
        "cargo": self.cargo
    }