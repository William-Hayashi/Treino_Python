##Exercício: Maior número em uma lista

##Escreva um programa em Python que receba uma lista de números inteiros como entrada e retorne o maior número presente na lista.

##Exemplo de entrada/saída:

entrada = input("Digite os números da lista: ")

lista = [int(lista) for lista in entrada.split()]

maximo = max(lista)

print("O maior número da lista é o número: {}".format(maximo))