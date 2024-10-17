#!/usr/bin/env python3

import sys

# Função principal
def main():
    # Verificar se o número de argumentos está correto
    if len(sys.argv) != 8:
        print("Erro: Você deve fornecer 7 argumentos: uma sequência de DNA e 6 números inteiros.")
        sys.exit(1)

    #Entrada de argumentos na linha de comando
    dna_seq = sys.argv[1]
    n1, n2, n3, n4, n5, n6 = sys.argv[2:8]

    #Verificando se os números são inteiros
    try:
        n1, n2, n3, n4, n5, n6 = int(n1), int(n2), int(n3), int(n4), int(n5), int(n6)
    except ValueError:
        print("Erro: os números inputados devem ser números inteiros.")
        sys.exit(1)

    #Verificando se os números estão continos no lenght da sequencia
    if max(n1, n2, n3, n4, n5, n6) > len(dna_seq):
        print("Erro: Um ou mais números fornecidos são maiores que o comprimento da sequencia.")
        sys.exit(1)

    #Extrair CDS1, CDS2 e CDS3
    cds1 = dna_seq[n1-1:n2] #subtraímos 01 devido à indexação do python, que se inicia em zero.
    cds2 = dna_seq[n3-1:n4]
    cds3 = dna_seq[n5-1:n6]

    #Conferindo se CDS' inicia com ATG
    if not cds1.startswith("ATG"):
        prin("Erro: A CDS1 não começa com o códon de início 'ATG'.")
        sys.exit(1)

    #Conferindo se CDS3 termia com o códom de parada TAG, TAA ou TGA
    if not (cds3.endswith("TAG") or cds3.endswith("TAA") or cds3.endswith("TGA")):
        print("Erro: A CDS3 não termina com um códon de parada válido (TAG, TAA ou TGA).")
        sys.exit(1)

    #Se todas as verificações forem válidas, concatenar as CDS e imprimir
    final_seq = cds1 + cds2 + cds3
    print(f"A sequencia que codifica a proteína é: {final_seq}")

#Executar a função
if __name__ == "__main__":
    main()

