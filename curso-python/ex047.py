# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1,51):
    print(f'\033[31m{c}\033[m' if c%2 == 0 else c)
