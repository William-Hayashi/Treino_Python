'''Exercício: Gerenciador de Tarefas

Crie um programa que permita ao usuário gerenciar suas tarefas diárias. O programa deve ser capaz de realizar as seguintes operações:

Adicionar uma nova tarefa à lista.
Remover uma tarefa existente da lista.
Marcar uma tarefa como concluída.
Exibir todas as tarefas na lista, indicando quais estão concluídas e quais ainda estão pendentes.
O programa deve continuar rodando até que o usuário decida sair.

Dicas:

Utilize uma lista para armazenar as tarefas.
Pode ser útil criar uma função para cada operação (adicionar, remover, marcar como concluída, exibir).
Utilize loops para manter o programa em execução até que o usuário decida sair.'''

tarefa = []

def adicionar():
    
    adicionar_tarefa = input("Qual tarefa deseja adicionar:")
    tarefa.append(adicionar_tarefa)
    print("Tarefa Adicionada! Deseja fazer mais algo?")
    return main()
        

def remover(tarefa):

    remover_tarefas = input("Digite a tarefa que deseja retirar: ")
    if remover_tarefas in tarefa:
        tarefa.remove(remover_tarefas)
        print("A tarefa: {} foi removida".format(remover_tarefas))
        return main()
    else:
        print("A tarefa não existe! Tente novamente")
        return remover()

def concluir(tarefa):
    
    concluir_tarefas = input("Digite a tarefa que deseja concluir: ")
    if concluir_tarefas in tarefa:
        tarefa.remove(concluir_tarefas)
        print("A tarefa: {} foi concluída".format(concluir_tarefas))
        return main()
    else:
        print("A tarefa não existe! Tente novamente")
        return concluir()
     

def exibir(tarefa):
    print("Aqui está a lista de tarefas: {}".format(tarefa))
    return main()

def main():
    print("************************************************************************************/n")
    resposta_primeira = input("Olá como vai! Deseja fazer alguma ação? Digite s ou n:")
    resposta_final = resposta_primeira.lower()

    if resposta_final == "s":
        while resposta_final == "s":

            print("(1) Adicionar Tarefa")
            print("(2) Remover Tarefa")
            print("(3) Concluir Tarefa")
            print("(4) Exibir Tarefa")
            print("(5) Sair")

            resposta = int(input("Digite o número que prefere!"))

            if resposta == 1:
                adicionar(resposta)
            elif resposta == 2:
                remover(resposta, tarefa)
            elif resposta == 3:
                concluir(resposta,tarefa)
            elif resposta == 4:
                exibir(resposta, tarefa)
            elif resposta == 5:
                break
            else:
                print("Opção inválida!")

    else: 
        print("Obrigado pela preferencia!")

if __name__ == "__main__":
    main()


