from storage import carregar_usuarios
from services import cadastro_usuario
from services import listar_usuarios

def mostrar_menu():
    print("\n=== Sistema de Cadastro ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("0 - Sair")

def main():
    usuarios = carregar_usuarios()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_usuario(usuarios)

        elif opcao == "2":
            listar_usuarios(usuarios)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
