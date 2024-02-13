entrada = input("DIgite a palavra: ")

palavra = entrada.lower()

vogais = ["a","e","i","o","u"]
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

contador = 0
consoantes = [letra for lentra in alfabeto if letra not in vogais]
    if consoantes in palavra:
    contador += 1



print("O número de consoantes é {}".format(contador))