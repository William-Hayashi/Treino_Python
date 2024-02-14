##Exercício: Soma dos Elementos de uma Lista

##Escreva um programa em Python que receba uma lista de números inteiros como entrada e calcule a soma de todos os elementos da lista.

##Exemplo de entrada/saída:

entrada = input("Digite os numeros com virgula")

lista = [int(numeros) for numeros in entrada.split()]

soma = sum(lista)

print (soma)