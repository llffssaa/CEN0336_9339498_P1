#!/usr/bin/env python3

def main():
    while True:
        try:
            P0 = float(input("Insira o tamanho inicial da população: "))
            if P0 <= 0:
                print("Por favor, insira um número positivo.")
                continue
            break
        except ValueError:
            print ("Entrada inválida. Por favor, insira um número válido.")

    while True:
        try:
            r = float(input("Insira a taxa de crescimento anual, em valores decimais: "))
            if r < 0:
                print("Por favor, insira um número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida")

    while True:
        try:
            t = int(input("Insira o número de anos para análise: "))
            if t < 0:
                print("Por favor, insira um número postivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


    for ano in range(1, t + 1):
        P_t = P0 * (1+r)**ano
        print(f"Ano {ano}: {P_t}")

if __name__ == "__main__":
    main()

