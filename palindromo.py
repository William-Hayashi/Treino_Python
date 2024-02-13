##Exercício: Palíndromo

##Escreva um programa em Python que verifique se uma palavra é um palíndromo ou não. Um palíndromo é uma palavra, frase, número ou outro tipo de sequência de caracteres que permanece a mesma quando lida de trás para frente.

##Exemplo de entrada/saída:

entrada = input("Digite a palavra")

palavra_invertida = entrada[::-1]

if palavra_invertida == entrada:
    print("A palavra é um palidromo")
else: 
    print("A palavra não é um palidromo")

