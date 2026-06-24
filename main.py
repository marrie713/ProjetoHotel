#importar as classes
# arquivo main funciona como a entrada do sistema/ menu e interação com usuário
from classes.hotel import Hotel

hotel = Hotel()

while True:

    print("\n===== HOTEL =====")
    print("1 - Cadastrar hóspede")
    print("2 - Cadastrar quarto")
    print("3 - Fazer reserva")
    print("4 - Quartos disponíveis")
    print("5 - Quartos ocupados")
    print("6 - Relatório")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")

        hotel.cadastrar_hospede(nome, cpf, telefone)

    elif opcao == "2":

        numero = input("Número: ")
        tipo = input("Tipo: ")
        valor = float(input("Valor da diária: "))

        hotel.cadastrar_quarto(numero, tipo, valor)

    elif opcao == "3":

        cpf = input("CPF do hóspede: ")
        numero = input("Número do quarto: ")
        dias = int(input("Dias: "))

        hotel.realizar_reserva(cpf, numero, dias)

    elif opcao == "4":

        hotel.listar_quartos_disponiveis()

    elif opcao == "5":

        hotel.listar_quartos_ocupados()

    elif opcao == "6":

        hotel.gerar_relatorio()

    elif opcao == "0":

        break