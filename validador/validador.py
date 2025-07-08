import re

def menu():
    while True:
        print("=== Validador de Dados ===")
        print("1. Validar E-mail")
        print("2. Validar Telefone")
        print("3. Validar CPF")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Validar email")
        elif opcao == "2":
            print("Validar Telefone")
        elif opcao == "3":
            print("Validar CPF")
        elif opcao == "4":
            print("Saindo do Validador. Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
