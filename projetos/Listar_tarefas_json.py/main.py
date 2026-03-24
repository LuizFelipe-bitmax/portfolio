from storage import carregar_tarefas,salvar_tarefas

def mostrar_menu():
    print("---Gerenciador de Tarefas---")
    print("1-Adicionar tarefas")
    print("2-Excluir tarefa")
    print("3-Listar tarefa")
    print("4-Concluir tarefa")
    print("0-Sair")

def adicionar_tarefas(tarefas):
    titulo = input("Coloque o titulo da tarefa:")

    tarefa = {
        "id" : len(tarefas) + 1,
        "titulo" : titulo,
        "concluida" : False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")
    return


def excluir_tarefa(tarefas):
    id_tarefa = int(input("Coloque o numero do ID que deseja excluir:"))
    try:
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefas.remove(tarefa)
                salvar_tarefas(tarefas)
                print("Tarefa foi excluida com sucesso!")
        print("Tarefa não encontrada")
    except ValueError:
        print("ID invalido")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Não tem nenhuma tarefa!!!")
        return
    for tarefa in tarefas:
        status = "sim" if tarefa["concluida"] else "não"
        print(f"ID:{tarefa["id"]}--Titulo:{tarefa["titulo"]}--Status:{status}")
    return

def concluir_tarefas(tarefas):
    id_identificador = int(input("Coloque o numero de id que você deseja concluir:"))
    try:    
        for tarefa in tarefas:
            if tarefa["id"] == id_identificador:
                tarefa["concluida"] == True
                salvar_tarefas(tarefas)
                print("Tarefa foi alterada com sucesso!!")
                return
        print("Não foi achada essa tarefa")
    except ValueError:
        print("ID invalido")

def main():
    pass
