#importar as classes
# arquivo main funciona como a entrada do sistema/ menu e interação com usuário
from backend.classes.hotel import Hotel

hotel = Hotel()

while True:
    print("\n========== HOTEL ==========")
    print("1 - Cadastrar hóspede")
    print("2 - Cadastrar funcionário")
    print("3 - Realizar reserva")
    print("4 - Listar hóspedes")
    print("5 - Listar funcionários")
    print("6 - Listar quartos disponíveis")
    print("7 - Listar quartos ocupados")
    print("8 - Listar reservas")
    print("9 - Finalizar reserva (Check-out)")
    print("10 - Gerar relatório")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")

        while True:
            cpf = input("CPF (Apenas números): ")

            if len(cpf) == 11:
                break
            else:
                print("CPF deve conter 11 dígitos!")

        while True:
            telefone = input("telefone: (Apenas números): ")

            if len(telefone) == 9:
                break
            else:
                print("Telefone deve conter 9 dígitos!")
                
        hotel.cadastrar_hospede(nome, cpf, telefone)

    elif opcao == "2":
        nome = input("Nome: ")

        while True:
            cpf = input("CPF (Apenas números): ")

            if len(cpf) == 11:
                break
            else:
                print("CPF deve conter 11 dígitos!")

        while True:
            telefone = input("telefone: (Apenas números): ")

            if len(telefone) == 9:
                break
            else:
                print("Telefone deve conter 9 dígitos!")

        cargo = input("Cargo: ")
        hotel.cadastrar_funcionario(nome, cpf, telefone, cargo)

    elif opcao == "3":
        cpf = input("CPF do hóspede: ")
        numero = int(input("Número do quarto (1 a 10): "))
        dias = int(input("Quantidade de diárias: "))
        hotel.realizar_reserva(cpf, numero, dias)

    elif opcao == "4":
        hotel.listar_hospedes()

    elif opcao == "5":
        hotel.listar_funcionarios()

    elif opcao == "6":
        hotel.listar_quartos_disponiveis()

    elif opcao == "7":
        hotel.listar_quartos_ocupados()

    elif opcao == "8":
        hotel.listar_reservas()

    elif opcao == "9":
        numero = int(input("Número do quarto: "))
        hotel.finalizar_reserva(numero)

    elif opcao == "10":
        hotel.gerar_relatorio()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")