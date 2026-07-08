import json
import os

class Persistencia:

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PASTA_DADOS = os.path.join(BASE_DIR, "dados")

    @staticmethod
    def salvar(nome_arquivo, dados):

        os.makedirs(Persistencia.PASTA_DADOS, exist_ok=True)

        caminho = os.path.join(Persistencia.PASTA_DADOS, nome_arquivo)

        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def carregar(nome_arquivo):

        caminho = os.path.join(Persistencia.PASTA_DADOS, nome_arquivo)

        if not os.path.exists(caminho):
            return []

        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)