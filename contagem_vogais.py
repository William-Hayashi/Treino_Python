##Exercício: Contagem de vogais

##Escreva um programa em Python que receba uma string como entrada e conte o número de vogais (a, e, i, o, u) presentes na string. Ignore maiúsculas e minúsculas, 
##ou seja, considere tanto 'a' quanto 'A' como vogais.

##Exemplo de entrada/saída:

entrada = input("Digite a palavra para contar a quantidade de vogais")

letras = entrada.lower()

vogais = [a,e,i,o,u]

contador = 0

for caractere in entrada:
    if caractere in vogais:
        contador += 1

print ("A quantidade de vogais é {}".format(contador)) 
