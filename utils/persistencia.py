import json

class Persistencia:

    @staticmethod
    def salvar(nome_arquivo, dados):

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4)

    @staticmethod
    def carregar(nome_arquivo):

        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)

        except FileNotFoundError:
            return []