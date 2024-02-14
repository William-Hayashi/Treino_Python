#Exercício: Maior e Menor Valor

#Escreva um programa em Python que recebe uma lista de números do usuário e encontra o maior e o menor valor nessa lista, exibindo ambos.

#Este exercício pode ajudar a praticar conceitos básicos de iteração sobre listas e comparação de valores.



    numeros_usuarios = input("Digite os 5 numeros, com virgula: ")
    numeros_reais = numeros_usuarios.split(",")]

    if len(numeros_reais) != 5:
        print("Por favor coloque um numero certo!")
    else:
        numeros_prontos = [float(numero)for numero in numeros_reais]

        maior = max(numeros_reais)
        menor = min(numeros_reais)
        
    print ("O número maior é: {}".format(maior))
    print ()"O número menor é: {}".format(menor))



