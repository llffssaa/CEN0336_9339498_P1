#!/usr/bin/env python3
#Import sys
import sys
#Definindo a função
def main ():
    if len(sys.argv) !=3:
        print("Erro: é necessário fornecer dois números inteiros positivos menores que 500.")
        return

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("Erro: os valores devem ser inteiros.")
        return

    #Se inteiros e menores que 500
    if a < 1 or a >=500 or b < 1 or b >= 500:
        print ("Erro: Os valores devem ser positivos e menores que 500.")
        return

    #Calcula o a**2 usando Pitágoras
    hipotenusa_quadrado = a**2 + b**2

    #Imprime o resultado
    print(f"O quadrado da hipotenusa para o triângulo retângulo com lados a = {a} e b = {b}, é {hipotenusa_quadrado}.")

# Chama a função principal
if __name__ == "__main__":
    main()

