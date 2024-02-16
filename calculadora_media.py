'''Exercício: Calculadora de Média

Crie um programa que pede ao usuário para digitar as notas de um aluno em três disciplinas diferentes (por exemplo, Matemática, Ciências e História). Em seguida, o programa deve calcular e exibir a média das três notas.

Instruções:

Utilize listas para armazenar as notas.
Solicite ao usuário que insira as notas para cada disciplina.
Calcule a média das notas utilizando as funções embutidas do Python.
Exiba o resultado da média ao usuário.
Este exercício ajuda a praticar o uso de listas em Python e operações básicas de cálculo.'''

ciencias = int(input("Digite a sua nota em Ciências: "))
matematica = int(input("Digite a sua nota em Matemática: "))
historia = int(input("Digite a sua nota em História: "))


numeros = [ciencias, matematica, historia]
soma = sum(numeros)
media_final = soma/len(numeros)
print(media_final)

