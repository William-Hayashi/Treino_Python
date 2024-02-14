#Exercício: Verificação de Números Pares

#Escreva um programa Python que recebe uma lista de números do usuário e verifica quantos desses números são pares. Em seguida, o programa deve exibir a quantidade de números pares encontrados.

#Este exercício pode ajudar a praticar a iteração sobre listas, condições e contagem de elementos.

entrada = input("Digite a lista de números, em vírgula")

lista = [int (numeros) for numeros in entrada.split(",")]

contador = 0

for numeros in lista:
    if numeros % 2 == 0:
        contador += 1

print("A quantidade de numeros pares é {}".format(contador))
        
