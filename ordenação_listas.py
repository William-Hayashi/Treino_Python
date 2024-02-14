"""Exercício: Ordenação de Lista de Números

Escreva um programa Python que recebe uma lista de números do usuário e ordene essa lista em ordem crescente ou decrescente, 
dependendo da escolha do usuário. Em seguida, exiba a lista ordenada.

Este exercício pode ajudar a praticar a manipulação de listas, bem como o uso de estruturas de controle de fluxo para lidar com diferentes opções do usuário."""


entrada_numeros = input("Digite a sequência de números, separado por vírgula")
entrada_ordem = input("Digite se deseja Crescente ou Decrescente")

lista_numeros = list(set[int(numeros)for numeros in entrada_numeros.split(",")])
opções_ordem = entrada_ordem.lower()

def main():
    if opções_ordem == "crescente":
        lista_numeros.sort()

    elif opções_ordem == "decrescente":
        lista_numeros.sort(reverse = True) 
    else:
        print("Digite uma a ordem de maneira correta")
        return
    
    print("A lista ordenada ficou assim: {}".format(lista_numeros))

main()


