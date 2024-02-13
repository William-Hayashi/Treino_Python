#Exercício: Média de uma lista

#Escreva um programa em Python que solicite ao usuário que insira uma lista de números inteiros separados por vírgula e, em seguida, calcule e exiba a média desses números.

#Exemplo de entrada/saída:

#Digite uma lista de números inteiros separados por vírgula: 10,20,30,40,50
#A média da lista é: 30.0


entrada = input("Digite uma lista de números separados por vírgula: ")

numeros = [int (numeros) for numeros in entrada.split(',')]

soma = sum(numeros)
media = soma/len(numeros)

print (media)

    