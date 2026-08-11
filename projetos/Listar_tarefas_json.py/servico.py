from storage import salvar_usuarios

def cadastro_usuario(usuarios):
    try:
        nome_usuario = input("Coloque o seu nome:")
        email_usuario = input("Coloque o seu email:")
        idade_usuario = int(input("Coloque a sua idade:"))
    except ValueError:
        return

    usuario = {
        "id" : len(usuarios) + 1,
        "nome" : nome_usuario,
        "email" : email_usuario,
        "idade" : idade_usuario,
        "ativo" : True
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    print("Usuario cadastrado!")

def listar_usuarios(usuarios):
    if not usuarios:
        return 
    for usuario in usuarios:
        print(f"ID:{usuario['id']}||Nome:{usuario['nome']}||Email:{usuario['email']}||Idade:{usuario['idade']}")

def excluir_usuario(usuarios):
    try:
        id_usuario = int(input("Coloque o ID:"))
        for usuario in usuarios:
            if usuario["id"] == id_usuario:
                usuarios.remove(usuario)
                salvar_usuarios(usuarios)
                print("Removido com sucesso")
                return
        print("Não foi achado nenhum com esse ID")
    except ValueError:
        print("Não foi achado esse ID")
