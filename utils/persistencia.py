import json
import os


class Persistencia:

    @staticmethod
    def salvar(nome_arquivo, dados):

        os.makedirs("dados", exist_ok=True)

        with open(f"dados/{nome_arquivo}", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def carregar(nome_arquivo):

        caminho = f"dados/{nome_arquivo}"

        if not os.path.exists(caminho):
            return []

        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)