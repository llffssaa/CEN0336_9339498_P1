#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 4:
        print("Para utilziar, insira a seguinte linha: ./script_popsim.py <P0> <r> <t>, onde: ")
        print("<P0>: Tamanho inicial da população (número positivo)")
        print("<r>: Taxa de crescimento anual (decimal, por exemplo, 0.05 para 5%)")
        print("<t>: Número de anos (número inteiro positivo)")
        sys.exit(1)
    try:
        P0 = float(sys.argv[1])
        r = float(sys.argv[2])
        t = int(sys.argv[3])

        if P0 < 0 or r < 0 or t < 0:
            print("Insira apenas valores positivos.")
            sys.exit(1)

    except ValueError:
        print("Entrada inválida. Insira números validos.")

    for ano in range(1, t + 1):
        P_t = P0 * (1+r)**ano
        print(f"Ano {ano}: {P_t}")

if __name__ == "__main__":
    main()

