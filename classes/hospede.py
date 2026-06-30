from classes.pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

    def exibir_dados(self):
        return (
            f"Hóspede\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self.telefone}"
        )
    
    def to_dict(self):
        return {
        "nome": self.nome,
        "cpf": self.cpf,
        "telefone": self.telefone
        }   