from views_tarefas import *


# FUNÇÃO PARA INTERAGIR COM USER
def main():
    while True:
        print('\n1. Adicionar tarefa')
        print('\n2. Visualizar tarefas')
        print('\n3. Marcar tarefa como concluída')
        print('\n4. Excluir tarefa')
        print('\n5. Sair')
        
        escolha = input("Digite a opção desejada (1 - 5): ")
        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            add_tarefas(descricao)
            print('Tarefa adicionada com sucesso')
            
        elif escolha == '2':
             tarefas = get_tarefas()
             if len(tarefas) == 0:
                 print("Nenhuma tarefa encontrada")
             else:
                 for tarefa in tarefas:
                     print(f"{tarefa[0]}. {tarefa[1]} - {'Concluida' if tarefa[2] else 'Incompleta'}") # tarefa[0] = id, tarefa[1] = nome
                 
        elif escolha == '3':
            id_tarefa = input("Digite o ID da tarefa: ")
            tarefa_concluida(id_tarefa)
            print("Tarefa marcada como concluída")
            
        elif escolha == '4':
            id_tarefa = input("Digite o ID da tarefa: ") 
            deletar_tarefa(id_tarefa)  
            print("Tarefa excluída")
            
        elif escolha == '5':
            break    
        
        else:
            print('Escolha uma opção inválida')
            
    meubd.close()       
    
if __name__ == "__main__":
    main()     
                        
            